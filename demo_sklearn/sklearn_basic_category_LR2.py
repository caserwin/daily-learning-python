#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-28 14:17
# @Author  : erwin
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import RandomizedLogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from common.util_function import *
import pandas as pd
import numpy as np
from sklearn.linear_model import RandomizedLogisticRegression
from sklearn.model_selection import train_test_split

"""
from sklearn.linear_model import RandomizedLogisticRegression
RandomizedLogisticRegression 显示过期，用 LogisticRegression(penalty='l1', solver="liblinear") 替代
"""

print_line("1. 数据探索")
df = pd.read_csv('./data/breast-cancer-wisconsin.data')
# print(df.info())
# print_br(df["Bare Nuclei"].value_counts())

print_line("2. 数据预处理")
# 众数填充
df["Bare Nuclei"].replace('?', df['Bare Nuclei'].mode()[0], inplace=True)
X = df.iloc[:, 1:10]
y = df.iloc[:, 10]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)

print_line("3. 特征转换")
# 归一化
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

print_line("4. 建立随机逻辑回归模型，筛选变量")
# rlr = RandomizedLogisticRegression()
rlr = LogisticRegression(penalty='l1', solver="liblinear")
rlr.fit(X_train, y_train)
support = [score > 0.25 for score in rlr.coef_[0]]
print_br(support)
print_br(u'有效特征为：%s' % ','.join(np.array(X.columns.values)[support]))

print_line("5. 基于筛选特征，构建逻辑回归模型")
x_selected_train = X_train[:, support]
x_selected_test = X_test[:, support]

lr = LogisticRegression(solver="liblinear")
lr.fit(x_selected_train, y_train)
y_predict = lr.predict(x_selected_test)

print_line("6. 评估展示")
print_br('Accuracy of LR Classifier:')
print_br(lr.score(x_selected_test, y_test))
print_br(classification_report(y_test, y_predict, target_names=['Benign', 'Malignant']))
