# -*- coding: utf-8 -*-
# @Time    : 2018/12/10 下午8:32
# @Author  : yidxue

from gensim.models.word2vec import Word2Vec

# 保证被考虑词语的最低频度
min_word_count = 1
num_featrues = 30
context = 4
downsampling = 1e-3

sentences = [['Hi', 'I', 'heard', 'about', 'Hadoop', 'Apache'],
             ['Hi', 'I', 'heard', 'about', 'Spark', 'Apache'],
             # ['I', 'wish', 'Java', 'could', 'use', 'case', 'classes'],
             # ['Logistic', 'regression', 'models', 'are', 'neat']
             ]
model = Word2Vec(min_count=min_word_count, size=num_featrues, sample=downsampling)

model.build_vocab(sentences)
model.train(sentences, total_examples=model.corpus_count, epochs=model.iter)

print(model['Hadoop'])
print(model['Spark'])

print(model.most_similar('Hadoop', topn=1))
print(model.most_similar('Spark', topn=1))
