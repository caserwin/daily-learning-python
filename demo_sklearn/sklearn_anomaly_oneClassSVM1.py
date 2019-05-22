#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/19 下午7:08
# @Author : Erwin
import matplotlib
import numpy as np

matplotlib.use('TkAgg')
from sklearn import svm
from common.util_function import *
from common.pickle_helper import store_model
from sklearn.model_selection import GridSearchCV

"""
https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM
"""
np.random.seed(41)


class MyOneClassSVM(svm.OneClassSVM):
    def score(self, X, y):
        # 采用准确率，作为score 计算方式
        pred = clf.predict(X)
        print(len(X))
        num = 0
        for i, j in zip(y, pred):
            if i == j:
                num = num + 1

        return num / len(pred)


print_line("1. 构建训练数据集")
normal_sample_count = 200
X = 0.5 * np.random.randn(normal_sample_count, 2)
normal_train = np.r_[X + 2, X - 2]
X_outliers = np.random.uniform(low=-4, high=4, size=(40, 2))

print_line("2. 训练和预测模型")
clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
clf.fit(normal_train)

print_line("3. 正样本评估")
normal_pred = clf.predict(normal_train)
print_br(normal_pred)

normal_error_num = 0
true_data = [1] * 200
for i, j in zip(true_data, normal_pred):
    if i != j:
        normal_error_num = normal_error_num + 1

print_br("正样本精确率")
print_br(1 - normal_error_num / len(normal_train))

print_line("4. 负样本评估")
outliers_normal_pred = clf.predict(X_outliers)
print_br(outliers_normal_pred)

outliers_error_num = 0
true_data = [-1] * 40
for i, j in zip(true_data, outliers_normal_pred):
    if i != j:
        outliers_error_num = outliers_error_num + 1

print_br("负样本精确率")
print_br(1 - outliers_error_num / len(X_outliers))

print_line("5. 存模型文件")
store_model(clf, "./model/one_class_svm.pkl")

print_line("6. 参数搜索")
model = MyOneClassSVM()
param_list = {'nu': np.arange(0.05, 1, 0.1),
              'kernel': ["rbf", "linear", "poly", "sigmoid"],
              "gamma": np.arange(0.01, 1, 0.1)}
gsearch = GridSearchCV(estimator=model, param_grid=param_list, cv=5, n_jobs=-1)
gsearch.fit(normal_train, [1] * 2 * normal_sample_count)

print_br(str(gsearch.best_params_) + "," + str(gsearch.best_score_))

print_line("7. 所有参数和相应评分")
for param, score in zip(gsearch.cv_results_['params'], gsearch.cv_results_['mean_test_score']):
    print(param, score)
