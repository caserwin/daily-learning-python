#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-20 21:21
# @Author  : erwin
import pandas as pd
from common.util_function import *
from common.pickle_helper import *
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from xgboost import XGBClassifier
from sklearn.preprocessing import OneHotEncoder

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 100)

print_line("1. 数据探索")
titanic = pd.read_csv('./data/titanic.txt')
X = titanic[['pclass', 'age', 'sex']]
y = titanic['survived']
# print(X.info())
# print(y.value_counts())

print_line("2. 数据预处理")
# 缺失值填充
X['age'].fillna(X['age'].mean(), inplace=True)
print(X.info())
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

print_line("3. 特征转换")
vec = DictVectorizer(sparse=False)
X_train = vec.fit_transform(X_train.to_dict(orient='record'))
X_test = vec.transform(X_test.to_dict(orient='record'))
# print(vec.feature_names_)
# print(type(X_train))

print_line("4. 采用XGBoost分类")
xgbc = XGBClassifier(n_estimators=100)
xgbc.fit(X_train[:, [0, 1, 3, 4]], y_train)
print(xgbc.score(X_test[:, [0, 1, 3, 4]], y_test))

'''
未经过特征选择，score 还不如经过特征选择
xgbc.fit(X_train, y_train)
print(xgbc.score(X_test, y_test))
'''
print(vec.feature_names_)
print(xgbc.feature_importances_)

store_model(xgbc, "./model/xgboost.pkl")

print_line("5. XGBoost 特征组合")
train_new_feature = xgbc.apply(X_train[:, [0, 1, 3, 4]])  # 与 n_estimators 值相同
print(train_new_feature.shape)
# print("新训练集的样本个数", len(train_new_feature))  # 与 n_estimators 值相同
# print("每个样本维度", len(train_new_feature[0]))
xgbenc = OneHotEncoder()
X_trans = xgbenc.fit_transform(train_new_feature)
print(X_trans.shape)
