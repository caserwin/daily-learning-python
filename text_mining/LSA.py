# -*- coding: utf-8 -*-
# @Time    : 2018/6/16 下午3:24
# @Author  : yidxue

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import Pipeline

documents = ["data/doc1.txt", "data/doc2.txt", "data/doc3.txt"]

# raw documents to tf-idf matrix:
vectorizer = TfidfVectorizer(stop_words='english', use_idf=True, smooth_idf=True)
# SVD to reduce dimensionality:
svd_model = TruncatedSVD(n_components=100, algorithm='randomized', n_iter=10)
# pipeline of tf-idf + SVD, fit to and applied to documents:
svd_transformer = Pipeline([('tfidf', vectorizer), ('svd', svd_model)])
svd_matrix = svd_transformer.fit_transform(documents)
