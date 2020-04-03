DATA_PATH="/Users/tarau/Desktop/sit/TEXT_CRAFTS/pytalk/bert/txt/"
SUMMARIES_PATH="/Users/tarau/Desktop/sit/TEXT_CRAFTS/pytalk/bert/abs/"
python3 summarize.py \
    --documents_dir $DATA_PATH \
    --summaries_output_dir $SUMMARIES_PATH \
    --no_cuda true \
    --batch_size 4 \
    --min_length 50 \
    --max_length 200 \
    --beam_size 5 \
    --alpha 0.95 \
    --block_trigram true \
    --compute_rouge false
