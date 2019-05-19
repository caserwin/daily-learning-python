#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/19 下午2:08
# @Author : Erwin
from common.pickle_helper import read_model
import numpy as  np
# noinspection PyUnresolvedReferences
from sklearn.neighbors import LocalOutlierFactor
# noinspection PyUnresolvedReferences
from sklearn.ensemble import IsolationForest

lof_model = read_model("./sklearn_LOF_demo1.pkl")
if_model = read_model("./sklearn_IsolationForest_demo1.pkl")

user_define = np.array([(2, 3), (5, 6), (2.3, 1.8)])
# -1表示异常点，1表示正常点。
print(lof_model.predict(user_define))
print(if_model.predict(user_define))