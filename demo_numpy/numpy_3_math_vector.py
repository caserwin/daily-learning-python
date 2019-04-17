#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-17 15:58
# @Author  : erwin
import numpy as np
from demo_pandas.function.util_function import *

np.set_printoptions(precision=2)

arr1 = np.linspace(0, 50, 9).reshape((3, 3))
arr2 = np.linspace(50, 100, 9).reshape((3, 3))
print_line("原始数据")
print_br(arr1)
print_br(arr2)

print_line("加减乘除")
print_br(np.add(arr1, arr2))
print_br(np.subtract(arr1, arr2))
print_br(np.multiply(arr1, arr2))
print_br(np.divide(arr1, arr2))

print_line("平方以及开方")
print_br(np.power(arr1, 2))
print_br(np.sqrt(arr1))

print_line("sin/cos/log/abs")
print_br(np.sin(arr1))
print_br(np.cos(arr1))
# print_br(np.log(arr1))
print_br(np.abs(arr1))

print_line("向上取整/向下取整/四舍五入")
print_br(np.ceil(arr1))
print_br(np.floor(arr1))
print_br(np.round(arr1))
