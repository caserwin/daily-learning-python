#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-31 13:26
# @Author  : erwin
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from common.util_function import *
import numpy as np
import pandas as pd

data = pd.read_csv('./data/voice.csv')
data.label = np.where(data.label.values == 'female', 1, 0)
X = data.drop('label', axis=1)
y = data.label

print_line("1. 特征选择建模")
rfe = RFE(LogisticRegression(solver='liblinear'), n_features_to_select=1)
rfe.fit(X, y)

print_line("2. 选择最优几个特征")
scores = []
num_features = len(X.columns)
for i in range(num_features):
    scores.append((rfe.ranking_[i], X.columns[i]))

print_best_worst(scores)
