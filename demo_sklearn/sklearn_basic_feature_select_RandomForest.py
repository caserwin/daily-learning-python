#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/19 下午3:21
# @Author : Erwin
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
from common.util_function import *

"""
http://www.cnblogs.com/xiaochouk/p/8583255.html
思想：看每个特征在随机森林中的每棵树上做了多大的贡献，然后取平均值，最后比较不同特征之间的贡献大小。
"""
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 100)

print_line("1. 显示原始数据")
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75
df['label'] = iris.target
print_br(df.head())

print_line("2. 构建训练数据和测试数据")
train, test = df[df['is_train'] == True], df[df['is_train'] == False]
features = df.columns[:4]

print_line("3. 开始训练")
clf = RandomForestClassifier(n_estimators=100, random_state=0, n_jobs=-1)
y = train['label'].values
clf.fit(train[features], y)

print_line("4. 特征重要性")
print_br(clf.feature_importances_)
