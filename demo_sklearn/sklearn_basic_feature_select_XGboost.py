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
from sklearn import metrics
from xgboost import plot_importance

# from matplotlib import pyplot as plt
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

# X = titanic[['pclass', 'age', 'sex', 'embarked', 'ticket', 'room']]
X = titanic[['pclass', 'age', 'sex']]
y = titanic['survived']

print_line("2. 数据预处理")
# 缺失值填充
X['age'].fillna(X['age'].mean(), inplace=True)
# X['embarked'].fillna(X['embarked'].mode()[0], inplace=True)
# X.loc[:, 'ticket'] = X['ticket'].map(lambda x: 0 if x is None else 1)
# X.loc[:, 'room'] = X['room'].map(lambda x: 0 if x is None else 1)

print(X.info())
print_br(X.describe(include="all"))

print_line("3. 特征转换")
vec = DictVectorizer(sparse=False)
X_all = vec.fit_transform(X.to_dict(orient='record'))
feature_index = dict(zip(vec.feature_names_, range(len(vec.feature_names_))))

print_line("4. 采用XGBoost选择特征")
xgbc = XGBClassifier()
xgbc.fit(X_all, y)

# pyplot.bar(range(len(xgbc.feature_importances_)), xgbc.feature_importances_)
# pyplot.show()

# plot_importance(xgbc)
# plt.show()

feature = {fn: fi for fn, fi in zip(vec.feature_names_, xgbc.feature_importances_)}
sort_value = OrderedDict(sorted(feature.items(), key=lambda kv: kv[1], reverse=True))
print(sort_value)

print_line("5. 前n个特征，对应的准确率/AUC")
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

print_line("6. 对AUC 排序，且去掉最低的remove_min_features 个 AUC值后，求平均AUC")
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


# print(auc_list)
# print(auc_list_sort)
auc_mean = average(auc_list_sort[:remove_min_features])
top_feature_num = 0
for i in range(len(auc_list)):
    if auc_list[i] > auc_mean:
        top_feature_num = i + 1
        break

# print(auc_mean)
top_features = dict_slice(sort_value, 0, top_feature_num)
top_features_index = [feature_index[k] for k, v in top_features.items()]
print(top_features)
print('对于一条新的数据 \t',vec.feature_names_, "选择特征index \t", top_features_index)
