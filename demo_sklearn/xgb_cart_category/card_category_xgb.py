#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/4 4:32 PM
# @Author : Erwin
import pandas as pd
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

np.set_printoptions(formatter={'float_kind': lambda x: "%.2f" % x})

# 读数据
source_df = pd.read_csv('../data/bank-full.csv', sep=";")

X = source_df[source_df.columns.values[:-1]]
y = source_df[source_df.columns.values[-1]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

vec = DictVectorizer(sparse=False)

X_train_dicv = vec.fit_transform(X_train.to_dict(orient='record'))
X_test_dicv = vec.transform(X_test.to_dict(orient='record'))

feature_index = dict(zip(vec.feature_names_, range(len(vec.feature_names_))))

print(feature_index)

xgbc = XGBClassifier()
xgbc.fit(X_train_dicv[:, [feature_index.get('poutcome=success')]], y_train)

print(xgbc.score(X_test_dicv[:, [feature_index.get('poutcome=success')]], y_test))
print(xgbc.feature_importances_)
