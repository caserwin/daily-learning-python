# !/usr/bin/python
# -*- coding:utf-8 -*-
import numpy as np
from sklearn.neighbors import LocalOutlierFactor
from common.util_function import *

"""
https://blog.csdn.net/YE1215172385/article/details/79766906
https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html
"""

np.random.seed(42)

print_line("1. 构建训练数据集")
X = 0.3 * np.random.randn(100, 2)
X_outliers = np.random.uniform(low=-4, high=4, size=(20, 2))
X_train = np.r_[X + 2, X - 2, X_outliers]

print_line("2. 训练和预测模型")
clf = LocalOutlierFactor(n_neighbors=15, contamination=0.1)
# 返回一个数组，-1表示异常点，1表示正常点。
y_pred = clf.fit_predict(X_train)
print_br(y_pred)

print_line("3. 结果评估")
error_num = 0
true_data = [1] * 200 + [-1] * 20
for i, j in zip(true_data, y_pred):
    if i != j:
        error_num = error_num + 1

recall_num = 0
for i, j in zip([-1] * 20, y_pred[200:]):
    if i != j:
        recall_num = recall_num + 1

print_br("准确率")
print_br(1 - error_num / 220)

print_br("召回率")
print_br(1 - recall_num / 20)
