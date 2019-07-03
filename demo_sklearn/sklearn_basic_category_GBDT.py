#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-20 21:21
# @Author  : erwin
import pandas as pd
from common.util_function import *
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import GradientBoostingClassifier

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 100)

"""
https://www.cnblogs.com/pinard/p/6143927.html
"""
print_line("1. 数据探索")
titanic = pd.read_csv('./data/titanic.txt')
X = titanic[['pclass', 'age', 'sex']]
y = titanic['survived']

print_line("2. 数据预处理")
# 缺失值填充
X['age'].fillna(X['age'].mean(), inplace=True)

print_line("3. 特征转换")
vec = DictVectorizer(sparse=False)
X_all = vec.fit_transform(X.to_dict(orient='record'))

print_line("4. GBDT 分类")
gbdt = GradientBoostingClassifier(n_estimators=100)
gbdt.fit(X_all, y)

y_pred = gbdt.predict(X_all)
print(','.join([str(i) for i in y_pred]))

print_line("5. GBDT 特征组合")
train_new_feature = gbdt.apply(X_all).reshape(-1, 100)  # 与 n_estimators 值相同
print(len(train_new_feature[0]))
print(len(train_new_feature))
