# Abstractive BERT-based Text Summarizer

A BERT-based summarizer, centered towards a simple API: some text in, a summary out, both strings. Also at pypi.org as package ```sumbert```.

## Installation:

```pip3 install sumbert```

or if you want ot play with the code, after cloning this, and going into the resulting folder, install as an editable package with:

```pip3 install -e .```


## Usage:

```
$ python3 -i
>>> from sumbert import summarize
>>> 
>>> text= """... your favorite story ..."""
>>> print(summarize(text))
```

This package is designed as a  simple API for an otherwise fairy intricate set of components. 

## Credits:

The code is derived from the ```bertabs``` submodule in  the HuggingFace transformers package at

[https://github.com/huggingface/transformers](https://github.com/huggingface/transformers)

which credits the abstractive summarization described in the  article [Text Summarization with Pretrained Encoders](https://arxiv.org/pdf/1908.08345.pdf) by [Yang Liu](https://nlp-yang.github.io/) and [Mirella Lapata](https://homepages.inf.ed.ac.uk/mlap/). 

The original code described in the article can be found on the Yang Liu's [github repository](https://github.com/nlpyang/PreSumm).

