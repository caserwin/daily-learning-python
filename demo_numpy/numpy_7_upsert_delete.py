#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-17 15:48
# @Author  : erwin
import numpy as np
from demo_pandas.function.util_function import *

np.set_printoptions(precision=3)

arr = np.linspace(0, 100, 10).reshape((5, 2))
print_line("原始数据")
print_br(arr)

print_line("增加一行/列到末尾")
print_br(np.append(arr, [[1, 2]], axis=0))
print_br(np.insert(arr, 2, [[2, 2, 2, 2, 2]], axis=1))

print_line("删除指定index的行/列")
print_br(np.delete(arr, 3, axis=0))
print_br(np.delete(arr, 1, axis=1))

print_line("更新行")
arr[1] = 4
print_br(arr)

print_line("更新元素")
arr[1, 1] = 5
print_br(arr)
