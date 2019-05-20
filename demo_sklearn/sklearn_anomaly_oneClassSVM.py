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

"""
https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM
"""
np.random.seed(42)

print_line("1. 构建训练数据集")
X = 0.3 * np.random.randn(100, 2)
X_outliers = np.random.uniform(low=-4, high=4, size=(20, 2))
train = np.r_[X + 2, X - 2, X_outliers]

print_line("2. 训练和预测模型")
clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
clf.fit(train)
pred = clf.predict(train)
print_br(pred)

print_line("3. 结果评估")
error_num = 0
true_data = [1] * 200 + [-1] * 20
for i, j in zip(true_data, pred):
    if i != j:
        error_num = error_num + 1

recall_num = 0
for i, j in zip([-1] * 20, pred[200:]):
    if i != j:
        recall_num = recall_num + 1

TP_FP = len(list(filter(lambda num: True if num == -1 else False, pred)))
TP = len(list(filter(lambda num: True if num == -1 else False, pred[200:])))
TP_FN = 20

print_br("精确率")
print_br(1 - error_num / 220)

print_br("准确率")
print_br(TP / TP_FP)

print_br("召回率")
print_br(TP / TP_FN)

print_line("4. 使用自定义的数据")
user_define = np.array([(2, 3), (5, 6), (2.3, 1.8)])
# -1表示异常点，1表示正常点。
print(clf.predict(user_define))

print_line("5. 存模型文件")
store_model(clf, "./model/one_class_svm.pkl")
