#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-17 15:19
# @Author  : erwin
import numpy as np
from demo_pandas.function.util_function import *

np.set_printoptions(precision=3)

arr = np.linspace(0, 100, 10).reshape((5, 2))
print_line("原始数据")
print_br(arr)

print_line("Returns number of elements in arr")
print_br(arr.size)

print_line("Returns dimensions of arr (rows,columns)")
print_br(arr.shape)

print_line("Returns type of elements in arr")
print_br(arr.dtype)

print_line("Convert arr elements to type dtype")
print_br(arr.astype(int))

print_line("Convert arr to a Python list")
print_br(arr.tolist())

print_line("View documentation for np.eye")
np.info(np.eye)

