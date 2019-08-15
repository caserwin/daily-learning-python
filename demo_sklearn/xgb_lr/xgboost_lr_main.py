#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/3 4:39 PM
# @Author : Erwin
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import OneHotEncoder
from xgboost import XGBClassifier
from demo_sklearn.xgb_lr.feature_important import FeatureSelect
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
    x = pd.DataFrame(data=X_all, columns=vec.feature_names_)[list(features.keys())]

    # 用新选择的特征，来做参数搜索
    print("开始参数搜索")
    param_list = {'max_depth': range(3, 10, 1),
                  "learning_rate": np.arange(0.05, 0.15, 0.01),
                  }

    model = XGBClassifier(random_state=10)
    gsearch = GridSearchCV(estimator=model, scoring="roc_auc", param_grid=param_list, cv=5, n_jobs=-1)
    gsearch.fit(x.values, y.values.ravel())
    print("最佳参数和相应评分", str(gsearch.best_params_) + "," + str(gsearch.best_score_))

    print("基于最好的参数进行训练")
    xgb = XGBClassifier(
        # max_depth=gsearch.best_params_["max_depth"],
        # learning_rate=gsearch.best_params_["learning_rate"],
        max_depth=4,
        learning_rate=0.1,
        random_state=10
    )

    xgb.fit(x.values, y.values.ravel())

    print("模型评估")
    y_pro = xgb.predict_proba(x.values)[:, 1]
    print("Accuracy: %.7f" % (xgb.score(x.values, y.values.ravel())))
    print("AUC Score : %f" % metrics.roc_auc_score(y.values.ravel(), y_pro))

    print("XGboost 特征转化")
    x_leaves = xgb.apply(x.values)
    print(x_leaves.shape)

    xgbenc = OneHotEncoder()
    X_trans = xgbenc.fit_transform(x_leaves)
    print(X_trans.shape)

    print("定义LR模型，开始参数搜索")
    param_list = {'C': [0.001, 0.01, 0.1, 1, 10, 100],
                  "penalty": ["l1", "l2"]
                  }

    model = LogisticRegression(random_state=10)
    gsearch = GridSearchCV(estimator=model, scoring="roc_auc", param_grid=param_list, cv=5, n_jobs=-1)
    gsearch.fit(x.values, y.values.ravel())
    print("最佳参数和相应评分", str(gsearch.best_params_) + "," + str(gsearch.best_score_))

    lr = LogisticRegression(
        C=gsearch.best_params_["C"],
        penalty=gsearch.best_params_["penalty"],
        random_state=10
    )

    lr.fit(X_trans, y.values.ravel())
    lr_y_pro = lr.predict_proba(X_trans)[:, 1]
    print("Accuracy: %.7f" % (lr.score(X_trans, y.values.ravel())))
    print("LR AUC Score : %f" % metrics.roc_auc_score(y.values.ravel(), lr_y_pro))
