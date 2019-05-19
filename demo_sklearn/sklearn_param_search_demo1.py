#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/19 下午4:46
# @Author : Erwin
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from common.util_function import *

np.random.seed(44)

print_line("1. 显示原始数据")
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75
df['label'] = iris.target
print_br(df.head())

print_line("2. 构建训练数据和测试数据")
train, test = df[df['is_train'] == True], df[df['is_train'] == False]
X = train[df.columns[:4]]
y = train['label'].values

print_line("3. 多个参数搜索")
param_test = {'max_depth': range(3, 10, 1), 'n_estimators': range(12, 60, 1)}
gsearch = GridSearchCV(estimator=RandomForestClassifier(max_features='sqrt', oob_score=True, random_state=10),
                       param_grid=param_test, iid=False, cv=5, n_jobs=-1)
"""
grid.fit()：运行网格搜索
cv_results_：给出不同参数情况下的评价结果
best_params_：描述了已取得最佳结果的参数的组合
best_score_：成员提供优化过程期间观察到的最好的评分
"""
gsearch.fit(X, y)
print_br("最佳参数和相应评分")
print_br(str(gsearch.best_params_) + "," + str(gsearch.best_score_))

print_br("所有参数和相应评分")
for param, score in zip(gsearch.cv_results_['params'], gsearch.cv_results_['mean_test_score']):
    print(param, score)
