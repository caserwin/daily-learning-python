#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/28 1:44 PM
# @Author : Erwin
from keras.models import load_model
from demo_keras.model.mmoe import MMoE
import keras as k
import numpy as np

print(k.__version__)



model = load_model('store/my_model', custom_objects={'MMoE': MMoE})
# Print out model architecture summary
model.summary()

# 生成 100 * 1 的 numpy array，进行预测。
arr = np.random.randn(1, 100)
prediction = model.predict(arr)
print(prediction)