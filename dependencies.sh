#!/usr/bin/bash
python -m textblob.download_corpora &
python -m spacy download en_core_web_sm