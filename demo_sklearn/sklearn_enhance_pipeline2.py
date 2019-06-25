#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-31 10:19
# @Author  : erwin
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd

data = pd.read_csv('./data/voice.csv')
data.label = np.where(data.label.values == 'female', 1, 0)
X = data.drop('label', axis=1)
y = data.label

param_grid = {'logisticregression__C': [0.001, 0.01, 0.1, 1, 10, 100]}
pipe = make_pipeline(StandardScaler(), LogisticRegression(penalty='l1', solver='liblinear'))
grid = GridSearchCV(pipe, param_grid, cv=10)
grid.fit(X, y)
print(grid.best_params_)
