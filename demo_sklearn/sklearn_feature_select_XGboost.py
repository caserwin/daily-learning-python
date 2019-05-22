#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-20 21:20
# @Author  : erwin
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from xgboost import XGBClassifier
from common.util_function import *
from sklearn.feature_selection import SelectFromModel
from collections import OrderedDict
from sklearn.model_selection import train_test_split

'''
https://blog.csdn.net/waitingzby/article/details/81610495
'''

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

print_line("3. 特征转换")
vec = DictVectorizer(sparse=False)
X_all = vec.fit_transform(X.to_dict(orient='record'))

print_line("4. 采用XGBoost选择特征")
xgbc = XGBClassifier()
xgbc.fit(X_all, y)

# from matplotlib import pyplot
# pyplot.bar(range(len(xgbc.feature_importances_)), xgbc.feature_importances_)
# pyplot.show()

feature = {fn: fi for fn, fi in zip(vec.feature_names_, xgbc.feature_importances_)}
sort_value = OrderedDict(sorted(feature.items(), key=lambda kv: kv[1], reverse=True))
print(sort_value)

print_line("5. 前n个特征，对应的准确率")
for thresh in sort_value.values():
    selection = SelectFromModel(xgbc, threshold=thresh, prefit=True)
    X_train, X_test, y_train, y_test = train_test_split(X_all, y, test_size=0.25)
    # X_train, X_test, y_train, y_test = train_test_split(X_all, y, test_size=0.25, random_state=1)

    select_X_train = selection.transform(X_train)
    select_X_test = selection.transform(X_test)

    # train model
    selection_model = XGBClassifier()
    selection_model.fit(select_X_train, y_train)

    print("Thresh=%.3f, n=%d, Accuracy: %.7f" % (
        thresh, select_X_train.shape[1], selection_model.score(select_X_test, y_test)))
