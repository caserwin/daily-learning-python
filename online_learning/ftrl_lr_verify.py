#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/23 9:58 AM
# @Author : Erwin
import pandas as pd
from common.util_function import *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 100)

print_line("1. 数据探索")
df = pd.read_csv('./data_train.txt', sep=' ')
df.columns = ["col2", "col3", "col4", "col5", "label"]

X_train = df[["col2", "col3", "col4", "col5"]]
y_train = df[["label"]]

lr = LogisticRegression(penalty='l2', solver="liblinear", max_iter=100)
lr.fit(X_train, y_train)

print_line("2. 评估")
df1 = pd.read_csv('./data_test.txt', sep=' ')
df1.columns = ["col2", "col3", "col4", "col5", "label"]

X_test = df1[["col2", "col3", "col4", "col5"]]
y_test = df1[["label"]]

# y_predict = lr.predict(X_test)

# print(y_predict)
# print(y_test.values.reshape(-1, ))

print_br(lr.score(X_test, y_test))
