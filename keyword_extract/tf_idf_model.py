# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 上午11:19
# @Author  : yidxue
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


class TFIDF(object):

    def __init__(self, corpus):
        self.corpus = corpus

    def getResult(self, top_k=1000):
        """
        :return:
        """
        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(self.corpus)
        print(X.toarray())

        # 类调用
        transformer = TfidfTransformer()
        tfidf = transformer.fit_transform(X)
        weight = tfidf.toarray()
        word = vectorizer.get_feature_names()

        objs = []
        for i in range(len(weight)):
            obj = []
            for j in range(len(word)):
                if weight[i][j] != 0:
                    obj.append((word[j], weight[i][j]))
            objs.append(obj)

        return [sorted(obj, key=lambda k_w: k_w[1], reverse=True)[0:top_k] for obj in objs]


if __name__ == '__main__':
    corpus = [
        "Ben Chan's Personal Personal Room",
        "Chris Kirushnamoorthy's Personal Room",
        'Agilent :: TP Galaxy Galaxy - bottom screen is down (couple of weeks) :: 1809I39228',
        'Discuss Incident INC0924190 - Vanity alias Name for Alias'
    ]

    objs_sort = TFIDF(corpus).getResult(top_k=10)
    for i in objs_sort:
        print(i)
