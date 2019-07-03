#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-22 20:04
# @Author  : erwin
import matplotlib as mpl
import xgboost as xgb
from common.util_function import *
mpl.use('TkAgg')
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.feature_extraction import DictVectorizer

print_line("1. 数据探索")
titanic = pd.read_csv('./data/titanic.txt')
X = titanic[['pclass', 'age', 'sex']]
y = titanic['survived']

print_line("2. 数据预处理")
# 缺失值填充
X['age'].fillna(X['age'].mean(), inplace=True)
print(X.info())
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

print_line("3. 特征转换")
vec = DictVectorizer(sparse=False)
X_train = vec.fit_transform(X_train.to_dict(orient='record'))
X_test = vec.transform(X_test.to_dict(orient='record'))

print_line("4. 采用XGBoost")
params = {
    'booster': 'gbtree',
    'objective': 'multi:softmax',
    'num_class': 3,
    'gamma': 0.1,
    'max_depth': 6,
    'lambda': 2,
    'subsample': 0.7,
    'colsample_bytree': 0.7,
    'min_child_weight': 3,
    'silent': 1,
    'eta': 0.1,
    'seed': 1000,
    'nthread': 4,
}

plst = params.items()

dtrain = xgb.DMatrix(X_train, y_train)
model = xgb.train(plst, dtrain, num_boost_round=500)

# 对测试集进行预测
dtest = xgb.DMatrix(X_test)
ans = model.predict(dtest)

# 计算准确率
cnt1 = 0
cnt2 = 0
for i in range(len(y_test)):
    if ans[i] == y_test.values[i]:
        cnt1 += 1
    else:
        cnt2 += 1

print("Accuracy: %.2f %% " % (100 * cnt1 / (cnt1 + cnt2)))

# 显示重要特征
# plot_importance(model)
# plt.show()
