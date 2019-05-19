#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/19 下午4:15
# @Author : Erwin
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
from common.util_function import *

"""
https://blog.csdn.net/cherdw/article/details/54971771
"""

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 100)

np.random.seed(44)

print_line("1. 显示原始数据")
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75
df['label'] = iris.target
print_br(df.head())

print_line("2. 构建训练数据和测试数据")
train, test = df[df['is_train'] == True], df[df['is_train'] == False]

features = df.columns[:4]
clf = RandomForestClassifier(n_estimators=13, max_depth=3, random_state=10, n_jobs=-1)
y = train['label'].values
clf.fit(train[features], y)
test_pred = clf.predict(test[features])

print_br("实际值")
print_br(test['label'].values)

print_br("预测值")
print_br(test_pred)

print_line("3. 评估展示")
preds = iris.target_names[test_pred]
res = pd.crosstab(test['label'], preds, rownames=['actual'], colnames=['preds'])
print_br(res)
