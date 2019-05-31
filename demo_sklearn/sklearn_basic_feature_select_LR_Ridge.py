#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-31 11:00
# @Author  : erwin
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from common.util_function import *
import numpy as np
import pandas as pd

data = pd.read_csv('./data/voice.csv')
data.label = np.where(data.label.values == 'female', 1, 0)
X = data.drop('label', axis=1)
y = data.label

print_line("1. 根据参数搜索器，来寻找模型最优参数")
param_grid = {'logisticregression__C': [0.001, 0.01, 0.1, 1, 10, 100]}
pipe = make_pipeline(StandardScaler(), LogisticRegression(penalty='l2', solver='liblinear'))
grid = GridSearchCV(pipe, param_grid, cv=10)
grid.fit(X, y)
print_br(grid.best_params_)

print_line("2. 拿到最优参数后，重新训练模型")
X_scaled = StandardScaler().fit_transform(X)
clf = LogisticRegression(penalty='l1', C=1, solver='liblinear')
clf.fit(X_scaled, y)

print_line("3. 根据第2步的模型来选择最优几个特征")
num_features = len(X.columns)
abs_feat = []
for i in range(num_features):
    coef = clf.coef_[0, i]
    abs_feat.append((abs(coef), X.columns[i]))

print_br(sorted(abs_feat, reverse=True))
print_best_worst(abs_feat)
