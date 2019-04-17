#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-17 21:11
# @Author  : erwin
import numpy as np
from demo_pandas.function.util_function import *

np.set_printoptions(precision=3)

arr1 = np.linspace(0, 50, 9).reshape((3, 3))
arr2 = np.linspace(50, 100, 9).reshape((3, 3))
print_line("原始数据")
print_br(arr1)
print_br(arr2)

print_line("行/列拼接")
print_br(np.concatenate((arr1, arr2), axis=0))
print_br(np.concatenate((arr1, arr2), axis=1))

print_line("行/列切分")
print_br(np.split(arr1, 3))
print_br(np.hsplit(arr1, 3))