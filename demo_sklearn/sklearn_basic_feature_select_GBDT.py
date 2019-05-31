#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-20 20:31
# @Author  : erwin
from sklearn.ensemble import GradientBoostingClassifier
import pandas as pd
from common.util_function import *

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 100)
"""
GradientBoostingClassifier(init=None, learning_rate=0.1, loss='deviance',
              max_depth=3, max_features=None, max_leaf_nodes=None,
              min_samples_leaf=1, min_samples_split=2,
              min_weight_fraction_leaf=0.0, n_estimators=100,
              random_state=None, subsample=1.0, verbose=0,
              warm_start=False)
"""

titanic = pd.read_csv('./data/titanic.txt')
print(titanic.head())

# gbdt = GradientBoostingClassifier()
# gbdt.fit(training_data, training_labels)
#
# print(gbdt.feature_importances_ )