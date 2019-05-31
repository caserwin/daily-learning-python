#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-22 19:45
# @Author  : erwin
from xgboost import XGBClassifier
from common.pickle_helper import *

model = read_model("./model/xgboost.pkl")
print(model.feature_importances_)
print(model.feature_importances_)
