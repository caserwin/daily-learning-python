#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-17 19:45
# @Author  : erwin
import numpy as np
from common.util_function import *
import matplotlib.pyplot as plt
np.set_printoptions(precision=3)

print_line("由随机数生成矩阵")
num = 11
# 设置随机数种子
np.random.seed(42)
X = np.random.randn(num // 2, 2)
print_br(X)

print_line("从一个左闭右开的均匀分布[low,high)中随机采样")
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.uniform.html
s = np.random.uniform(low=-6, high=6, size=(2, 2))
print_br(s)
