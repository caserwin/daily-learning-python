#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-17 20:01
# @Author  : erwin
import numpy as np
from common.util_function import *

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

print_line("多个向量间的集合操作")
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([3, 4, 5, 6, 7])
# 并集
print_br(np.union1d(arr1, arr2))
# 差集
print_br(np.setdiff1d(arr1, arr2, assume_unique=True))
# 交集
print_br(np.intersect1d(arr1, arr2, assume_unique=True))
