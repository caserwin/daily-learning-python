#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-17 16:32
# @Author  : erwin
import numpy as np
from common.util_function import *

np.set_printoptions(precision=0)

arr = np.linspace(0, 10, 9).reshape((3, 3))
print_line("原始数据")
print_br(arr)

print_line("切片索引")
print_br(arr[1])
print_br(arr[1, 1])
print_br(arr[0:2, 0:2])
print_br(arr[:2, ])

print_line("boolean 索引")
print_br((arr > 3) & (arr < 7))
print_br(~(arr > 3) & (arr < 7))
print_br(arr[[True, False, True]])

print_line("boolean 索引 + 切片操作")
print_br(arr[[True, False, True], 0:2])
print_br(arr[:, [True, False, True]])
