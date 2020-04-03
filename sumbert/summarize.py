'''
usage:
  summarize(text_made_of_your_sentences)
  returning summary as (an all lowercase) string
'''
from collections import namedtuple
from nltk.tokenize import sent_tokenize

import torch
from torch.utils.data import DataLoader, SequentialSampler
from .modeling_bertabs import BertAbs, build_predictor
from transformers import BertTokenizer

from .utils_summarization import (
    build_mask,
    compute_token_type_ids,
    encode_for_summarization,
    truncate_or_pad,
)

import argparse
args = argparse.Namespace(alpha=0.95,
                          batch_size=4,
                          beam_size=5,
                          block_trigram=True,
                          device="cpu",
                          max_length=200,
                          min_length=50,
                          no_cuda=True
                          )

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased", do_lower_case=True)
model = BertAbs.from_pretrained("bertabs-finetuned-cnndm")
model.to(args.device)
model.eval()

Batch = namedtuple("Batch", ["document_names", "batch_size", "src", "segs", "mask_src", "tgt_str"])

def summarize(sentences):
  '''
  Takes as input a string contaning sentences or
  a list of strings, one sentence each.
  Assuming sentences end with proper punctuation.
  '''
  if isinstance(sentences,str) :
    sentences=sent_tokenize(sentences)

  symbols = {
    "BOS": tokenizer.vocab["[unused0]"],
    "EOS": tokenizer.vocab["[unused1]"],
    "PAD": tokenizer.vocab["[PAD]"],
  }

  data_iterator = build_data_source(sentences,args, tokenizer)
  predictor = build_predictor(args, tokenizer, symbols, model)

  for batch in data_iterator:
    batch_data = predictor.translate_batch(batch)
    translations = predictor.from_batch(batch_data)
    summaries = [format_summary(t) for t in translations]

    return summaries[0]

def format_summary(translation):
    """ Transforms the output of the `from_batch` function
    into nicely formatted summaries.
    """
    raw_summary, _, _ = translation
    summary = (
        raw_summary.replace("[unused0]", "")
        .replace("[unused3]", "")
        .replace("[PAD]", "")
        .replace("[unused1]", "")
        .replace(r" +", " ")
        .replace(" [unused2] ", ". ")
        .replace("[unused2]", "")
        .strip()
    )
    return summary

def build_data_source(sentences,args,tokenizer) :
  dataset=[('temp.txt',sentences,[])]
  sampler=SequentialSampler(dataset)

  def collate_fn(data):
    #ppp(data)
    return collate(data, tokenizer, block_size=512, device=args.device)

  iterator = DataLoader(dataset, sampler=sampler, batch_size=args.batch_size, collate_fn=collate_fn, )

  return iterator

def collate(data, tokenizer, block_size, device):
    """ Collate formats the data passed to the data loader.

    In particular we tokenize the data batch after batch to avoid keeping them
    all in memory. We output the data as a namedtuple to fit the original BertAbs's
    API.
    """
    data = [x for x in data if not len(x[1]) == 0]  # remove empty_files
    names = [name for name, _, _ in data]
    encoded_text = [encode_for_summarization(story, tokenizer) for _, story, _ in data]
    encoded_stories = torch.tensor(
        [truncate_or_pad(story, block_size, tokenizer.pad_token_id) for story, _ in encoded_text]
    )
    encoder_token_type_ids = compute_token_type_ids(encoded_stories, tokenizer.cls_token_id)
    encoder_mask = build_mask(encoded_stories, tokenizer.pad_token_id)

    batch = Batch(
        document_names=names,
        batch_size=len(encoded_stories),
        src=encoded_stories.to(device),
        segs=encoder_token_type_ids.to(device),
        mask_src=encoder_mask.to(device),
        tgt_str=[''] #summaries,
    )

    return batch

def decode_summary(summary_tokens, tokenizer):
    """ Decode the summary and return it in a format
    suitable for evaluation.
    """
    summary_tokens = summary_tokens.to("cpu").numpy()
    summary = tokenizer.decode(summary_tokens)
    sentences = summary.split(".")
    sentences = [s + "." for s in sentences]
    return sentences

# helper for locating source of debug messages
def ppp(*args) :
  from inspect import getframeinfo, stack
  caller = getframeinfo(stack()[1][0])

  print('DEBUG:',
        caller.filename.split('/')[-1],
        '->',caller.lineno,end=': ')
  print(*args)

# simple test

sents='''
The virus, which was first reported in Wuhan, China, has spread to at 
least 181 countries and regions. The U.S. has more cases than any other country, 
with more than 234000 confirmed infections to date, followed by 
Italy (115000) and Spain (110000). 
All three countries have overtaken the number of cases in China, which now has 
a confirmed infected population of 82400 people.

While China has seen a rise in imported cases in recent days, 
the outbreak has been largely contained, with outbound travel restrictions 
now lifted in the Hubei province. Restrictions are also due to be 
lifted in Wuhan later this month.
But cases continue to soar outside China and the spread of the virus has been 
picking up pace in the U.S., the current global epicenter of the outbreak. 
New York continues to report the country's highest number of cases, with more 
than 83700 confirmed infections to date, including 47439 cases in New York City, 
the office of New York Governor Andrew Cuomo confirmed as of Wednesday.
'''

def run_test() :
  print('SUMMARY:')
  print(summarize(sents))

if __name__ == "__main__":
  run_test()
