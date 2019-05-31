#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-28 09:45
# @Author  : erwin
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
df = pd.read_csv('./data/breast-cancer-wisconsin.data')
# print(df.info())
# print_br(df["Bare Nuclei"].value_counts())

print_line("2. 数据预处理")
# 众数填充
df["Bare Nuclei"].replace('?', df['Bare Nuclei'].mode()[0], inplace=True)
# 数据分割
X = df.iloc[:, 1:10]
y = df.iloc[:, 10]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)
# print_br(y_test.value_counts())

print_line("3. 特征转换")
# 归一化
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

print_line("4. 采用逻辑回归")
lr = LogisticRegression(penalty='l2', solver="liblinear", max_iter=100)
lr.fit(X_train, y_train)
y_predict = lr.predict(X_test)

print_line("5. 评估展示")
print_br('Accuracy of LR Classifier:')
print_br(lr.score(X_test, y_test))
print_br(classification_report(y_test, y_predict, target_names=['Benign', 'Malignant']))
