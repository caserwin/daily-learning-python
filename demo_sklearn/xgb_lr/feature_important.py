#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/3 9:21 AM
# @Author : Erwin
from sklearn import metrics
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from collections import OrderedDict
from sklearn.feature_extraction import DictVectorizer
import pandas as pd
import numpy as np

np.set_printoptions(threshold=np.inf)


class FeatureSelect(object):

    def __init__(self, data, y, feature_names):
        self.xgbc = XGBClassifier()
        self.xgbc.fit(data, y)
        self.auc_list = []
        self.auc_mean = 0
        self.times = 2

        self.data = data
        self.y = y
        feature = {fn: fi for fn, fi in zip(feature_names, self.xgbc.feature_importances_)}
        self.sort_value = OrderedDict(sorted(feature.items(), key=lambda kv: kv[1], reverse=True))
        self.remove_min_auc = -int(len(feature_names) / 5)

    def get_auc_list_sort(self):
        for thresh in self.sort_value.values():
            selection = SelectFromModel(self.xgbc, threshold=thresh, prefit=True)
            X_train, X_test, y_train, y_test = train_test_split(self.data, self.y, test_size=0.25)
            # X_train, X_test, y_train, y_test = train_test_split(X_all, y, test_size=0.25, random_state=1)

            select_X_train = selection.transform(X_train)
            select_X_test = selection.transform(X_test)

            # train model
            selection_model = XGBClassifier()
            selection_model.fit(select_X_train, y_train)

            # y_pre = selection_model.predict(select_X_test)
            y_pro = selection_model.predict_proba(select_X_test)[:, 1]

            print("Thresh=%.3f, n=%d, Accuracy: %.7f" % (
                thresh, select_X_train.shape[1], selection_model.score(select_X_test, y_test)))
            # print("Accuracy : %.7g" % metrics.accuracy_score(y_test, y_pre))
            print("AUC Score : %f" % metrics.roc_auc_score(y_test, y_pro))
            self.auc_list.append(metrics.roc_auc_score(y_test, y_pro))
            print('-' * 10)

        auc_list_sort = self.auc_list.copy()
        auc_list_sort.sort(reverse=True)
        return auc_list_sort

    def _average(self, lst):
        return sum(lst) / len(lst)

    def _dict_slice(self, adict, start, end):
        keys = list(adict.keys())
        dict_slice = {}
        for k in keys[start:end]:
            dict_slice[k] = adict[k]
        return dict_slice

    def get_feature(self):
        auc_list_sort = self.get_auc_list_sort()
        self.auc_mean = self._average(auc_list_sort[:self.remove_min_auc])
        top_features = 0
        for i in range(len(self.auc_list)):
            if self.auc_list[i] > self.auc_mean:
                top_features = i + 1
                self.times = self.times - 1
            if self.times == 0:
                break
        return self._dict_slice(self.sort_value, 0, top_features)

    def get_auc_mean(self):
        return self.auc_mean


if __name__ == '__main__':
    source_df = pd.read_csv('../data/bank-full.csv', sep=";")

    X = source_df[source_df.columns.values[:-1]]
    y = source_df[source_df.columns.values[-1]]

    vec = DictVectorizer(sparse=False)
    X_all = vec.fit_transform(X.to_dict(orient='record'))
    fs = FeatureSelect(X_all, y, vec.feature_names_)
    print(fs.sort_value)
    print(fs.get_feature())
