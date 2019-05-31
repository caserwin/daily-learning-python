#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/20 上午10:16
# @Author : Erwin
import numpy as np
from sklearn import svm
from common.util_function import *
from common.pickle_helper import store_model

np.random.seed(41)

print_line("1. 构建训练数据集")
normal_sample_count = 200
X = 0.5 * np.random.randn(normal_sample_count, 2)
normal_train = np.r_[X + 2, X - 2]
X_outliers = np.random.uniform(low=-4, high=4, size=(40, 2))
print_br(normal_train)

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

print_line("5. 使用自定义的数据")
user_define = np.array([(2, 3), (5, 6), (2.3, 1.8)])
# -1表示异常点，1表示正常点。
print(clf.predict(user_define))

print_line("6. 存模型文件")
store_model(clf, "./model/one_class_svm_optimization.pkl")
