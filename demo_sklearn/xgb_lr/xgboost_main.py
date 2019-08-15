#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/3 10:55 AM
# @Author : Erwin
from demo_sklearn.xgb_lr.feature_important import FeatureSelect
from xgboost import XGBClassifier
from sklearn import metrics
import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.feature_extraction import DictVectorizer

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 100)

if __name__ == '__main__':
    source_df = pd.read_csv('../data/bank-full.csv', sep=";")

    X = source_df[source_df.columns.values[:-1]]
    y = source_df[source_df.columns.values[-1]]

    vec = DictVectorizer(sparse=False)
    X_all = vec.fit_transform(X.to_dict(orient='record'))

    print("开始特征选择")
    fs = FeatureSelect(X_all, y, vec.feature_names_)

    features = fs.get_feature()
    # print(fs.get_auc_mean())
    # TODO: 这里急需要看看 vec.feature_names_ 和 X_all 的列是否一一对应
    x = pd.DataFrame(data=X_all, columns=vec.feature_names_)[list(features.keys())]

    # 用新选择的特征，来做参数搜索
    print("开始参数搜索")
    param_list = {"max_depth": range(3, 10, 1),
                  "learning_rate": np.arange(0.05, 0.15, 0.01),
                  }

    model = XGBClassifier(random_state=10)
    gsearch = GridSearchCV(estimator=model, scoring="roc_auc", param_grid=param_list, cv=5, n_jobs=-1)
    gsearch.fit(x.values, y.values.ravel())

    print("所有参数和相应评分")
    for param, score in zip(gsearch.cv_results_['params'], gsearch.cv_results_['mean_test_score']):
        print(param, score)

    print("最佳参数和相应评分", str(gsearch.best_params_) + "," + str(gsearch.best_score_))

    print("基于最好的参数进行训练")
    xgb = XGBClassifier(
        # max_depth=gsearch.best_params_["max_depth"],
        # learning_rate=gsearch.best_params_["learning_rate"],
        max_depth=4,
        learning_rate=0.1
        # random_state=10
    )

    # X_train, X_test, y_train, y_test = train_test_split(x.values, y.values.ravel(), test_size=0.25)
    xgb.fit(x.values, y.values.ravel())

    print("模型评估")
    # y_pro = xgb.predict_proba(X_test)[:, 1]
    # print("Accuracy: %.7f" % (xgb.score(X_test, y_test)))
    # print("AUC Score : %f" % metrics.roc_auc_score(y_test, y_pro))

    y_pro = xgb.predict_proba(x.values)[:, 1]
    print("Accuracy: %.7f" % (xgb.score(x.values, y.values.ravel())))
    print("AUC Score : %f" % metrics.roc_auc_score(y.values.ravel(), y_pro))
