#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-24 10:22
# @Author  : erwin
from sklearn.feature_selection import VarianceThreshold
from sklearn import pipeline
from sklearn.preprocessing import StandardScaler, MinMaxScaler

X = [[0, 2, 0, 3], [0, 1, 4, 3], [1, 1, 1, 3]]
"""
每个算子，必须实现了fit() 和 transform() 方法
"""

scaler = pipeline.Pipeline(steps=[
    ('minmax', MinMaxScaler(feature_range=(-1, 1))),
    ('remove_constant', VarianceThreshold())
])

res = scaler.fit_transform(X)
print(res.shape)
print(res)
