#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-31 11:10
# @Author  : erwin
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2, mutual_info_classif
from common.util_function import *
import numpy as np
import pandas as pd

data = pd.read_csv('./data/voice.csv')
data.label = np.where(data.label.values == 'female', 1, 0)
X = data.drop('label', axis=1)
y = data.label

print_line("1. 特征选择建模")
# test = SelectKBest(score_func=chi2, k=2)
test = SelectKBest(score_func=mutual_info_classif, k=2)
test.fit(X, y)

print_line("2. 选择最优几个特征")
num_features = len(X.columns)
scores = []
for i in range(num_features):
    score = test.scores_[i]
    scores.append((score, X.columns[i]))

print_br(sorted(scores, reverse=True))
print_best_worst(scores)
