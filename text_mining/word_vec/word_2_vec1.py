#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/7 2:37 PM
# @Author : Erwin

from gensim.models import KeyedVectors
import simplejson as json
model = KeyedVectors.load_word2vec_format("/Users/xueyiding/数据/min.txt", binary=False)

if __name__ == '__main__':
    word = "红烧肉"
    if word in model.vocab:
        print({'word': word, 'vector': model.word_vec(word).tolist()})
        print({'word': word, 'top_similar_words': model.similar_by_word(word, topn=20, restrict_vocab=None)})
        word1 = "我"
        word2 = "你"
        print(json.dumps({'word1': word1, 'word2': word2, 'similarity': float(model.similarity(word1, word2))}, ensure_ascii=False))
    else:
        print("==")