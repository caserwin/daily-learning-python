#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-20 20:50
# @Author  : erwin
from sklearn.feature_extraction import DictVectorizer
import pandas as pd
from common.util_function import *

print_line("1. 原始数据")
data = [
    {'city': 'Dubai', 'temperature': 33.},
    {'city': 'London', 'temperature': 12.},
    {'city': 'San Fransisco', 'temperature': 18.},
]

df = pd.DataFrame(data=data)

print_line("2. 拟合模型")
vec = DictVectorizer(sparse=False)
# vec = DictVectorizer(sparse=True)  # transform 结果必须通过 .toarray() 转化为矩阵

vec.fit(df.to_dict(orient='record'))
print(vec.transform(df.to_dict(orient='record')))
print(vec.get_feature_names())

print_line("3. 拟合新的数据")
new_data = [
    {'city': 'London', 'temperature': 1},
    {'city': 'London1', 'temperature': 2}
]

print_br(vec.transform(new_data))
