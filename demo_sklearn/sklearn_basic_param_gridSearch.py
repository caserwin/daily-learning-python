#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/19 下午4:46
# @Author : Erwin
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import pandas as pd
from common.util_function import *

print(np.arange(0.05, 0.15, 0.01))

np.random.seed(44)
iris = load_iris()

print_line("RandomForest 多个参数搜索")
param_list = {'max_depth': range(3, 10, 1), 'n_estimators': range(15, 60, 1), "max_features": [None, "sqrt", "log2"]}

model = RandomForestClassifier()
# gsearch = GridSearchCV(estimator=model, scoring="f1", param_grid=param_list, cv=5, n_jobs=-1)
gsearch = GridSearchCV(estimator=model, param_grid=param_list, cv=5, n_jobs=-1)
gsearch.fit(iris.data, iris.target)

print_line("最佳参数和相应评分")
print_br(str(gsearch.best_params_) + "," + str(gsearch.best_score_))

print_line("所有参数和相应评分")
for param, score in zip(gsearch.cv_results_['params'], gsearch.cv_results_['mean_test_score']):
    print(param, score)

print_line("基于最好的参数进行训练")
rf = RandomForestClassifier(max_depth=gsearch.best_params_["max_depth"],
                            n_estimators=gsearch.best_params_["n_estimators"],
                            max_features=gsearch.best_params_["max_features"],
                            )
# rf = RandomForestClassifier(max_depth=3,
#                             n_estimators=27,
#                             max_features="log2",
#                             random_state=10)
rf.fit(iris.data, iris.target)

print_line("最优参数的随机森林预测和结果评估")
test_pred = rf.predict(iris.data)
preds = iris.target_names[test_pred]

res = pd.crosstab(iris.target, preds, rownames=['actual'], colnames=['preds'])
print_br(res)
