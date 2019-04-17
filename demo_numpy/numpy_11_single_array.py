#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-17 15:58
# @Author  : erwin
import numpy as np
from demo_pandas.function.util_function import *

np.set_printoptions(precision=3)

arr = np.linspace(0, 100, 10).reshape((2, 5))
print_line("原始数据")
print_br(arr)

print_line("单个array操作")
print_br(np.add(arr, 2))
print_br(np.subtract(arr, 2))
print_br(np.multiply(arr, 2))
print_br(np.divide(arr, 2))
print_br(np.power(arr, 2))

print_line("平方以及开方")
print_br(np.power(arr, 2))
print_br(np.sqrt(arr))

print_line("sin/cos/log/abs")
print_br(np.sin(arr))
print_br(np.cos(arr))
# print_br(np.log(arr1))
print_br(np.abs(arr))

print_line("向上取整/向下取整/四舍五入")
print_br(np.ceil(arr))
print_br(np.floor(arr))
print_br(np.round(arr))
