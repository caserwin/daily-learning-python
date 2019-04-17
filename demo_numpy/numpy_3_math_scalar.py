#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-17 15:57
# @Author  : erwin
import numpy as np
from demo_pandas.function.util_function import *

np.set_printoptions(precision=3)

arr = np.linspace(0, 100, 10).reshape((2, 5))
print_line("原始数据")
print_br(arr)

print_line("加减乘除及平方")
print_br(np.add(arr, 2))
print_br(np.subtract(arr, 2))
print_br(np.multiply(arr, 2))
print_br(np.divide(arr, 2))
print_br(np.power(arr, 2))
