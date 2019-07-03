#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/2 3:58 PM
# @Author : Erwin
from collections import OrderedDict

import pandas as pd
from sklearn import metrics
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from common.util_function import *

print_line("1. 数据探索")
source_df = pd.read_csv('../data/bank-full.csv', sep=";")

X = source_df[source_df.columns.values[:-1]]
y = source_df[source_df.columns.values[-1]]

print_line("2. 特征转换")
vec = DictVectorizer(sparse=False)
X_all = vec.fit_transform(X.to_dict(orient='record'))

print_line("3. 采用XGBoost选择特征")
xgbc = XGBClassifier()
xgbc.fit(X_all, y)

feature = {fn: fi for fn, fi in zip(vec.feature_names_, xgbc.feature_importances_)}
sort_value = OrderedDict(sorted(feature.items(), key=lambda kv: kv[1], reverse=True))
print(sort_value)

print_line("4. 前n个特征，对应的准确率/AUC")
auc_list = []
for thresh in sort_value.values():
    selection = SelectFromModel(xgbc, threshold=thresh, prefit=True)
    X_train, X_test, y_train, y_test = train_test_split(X_all, y, test_size=0.25)
    # X_train, X_test, y_train, y_test = train_test_split(X_all, y, test_size=0.25, random_state=1)

    select_X_train = selection.transform(X_train)
    select_X_test = selection.transform(X_test)

    # train model
    selection_model = XGBClassifier()
    selection_model.fit(select_X_train, y_train)

    y_pre = selection_model.predict(select_X_test)
    y_pro = selection_model.predict_proba(select_X_test)[:, 1]

    print("Thresh=%.3f, n=%d, Accuracy: %.7f" % (
        thresh, select_X_train.shape[1], selection_model.score(select_X_test, y_test)))
    # print("Accuracy : %.7g" % metrics.accuracy_score(y_test, y_pre))
    print("AUC Score : %f" % metrics.roc_auc_score(y_test, y_pro))
    auc_list.append(metrics.roc_auc_score(y_test, y_pro))
    print('-' * 10)

print_line("5. 对AUC 排序，且去掉最低的remove_min_features 个 AUC值后，求平均AUC")
remove_min_features = -2
auc_list_sort = auc_list.copy()
auc_list_sort.sort(reverse=True)


def average(lst):
    return sum(lst) / len(lst)


def dict_slice(adict, start, end):
    keys = list(adict.keys())
    dict_slice = {}
    for k in keys[start:end]:
        dict_slice[k] = adict[k]
    return dict_slice


print(auc_list)
# print(auc_list_sort)
auc_mean = average(auc_list_sort[:remove_min_features])
top_features = 0
for i in range(len(auc_list)):
    if auc_list[i] > auc_mean:
        top_features = i + 1
        break

print(auc_mean)
# print(top_features)
print(dict_slice(sort_value, 0, top_features))
