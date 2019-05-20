#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-17 19:45
# @Author  : erwin
import numpy as np
from common.util_function import *
np.set_printoptions(precision=3)
# 设置随机数种子
np.random.seed(42)

print_line("randn() 返回标准正太分布的数值")
print_br(np.random.randn(3))
print_br(np.random.randn(10, 2))


print_line("从一个左闭右开的均匀分布[low,high)中随机采样")
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.uniform.html
s = np.random.uniform(low=-6, high=6, size=(2, 2))
print_br(s)
