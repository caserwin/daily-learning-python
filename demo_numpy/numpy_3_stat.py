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

print_line("返回每行/列/所有数据的 mean")
print_br(np.mean(arr, axis=0))
print_br(np.mean(arr, axis=1))
print_br(np.mean(arr))

print_line("返回每行/列/所有数据的 sum")
print_br(np.sum(arr, axis=0))
print_br(np.sum(arr, axis=1))
print_br(np.sum(arr))

print_line("返回每行/列/所有数据的 min")
print_br(np.min(arr, axis=0))
print_br(np.min(arr, axis=1))
print_br(np.min(arr))

print_line("返回每行/列/所有数据的 max")
print_br(np.max(arr, axis=0))
print_br(np.max(arr, axis=1))
print_br(np.max(arr))

print_line("返回每行/列/所有数据的 var")
print_br(np.var(arr, axis=0))
print_br(np.var(arr, axis=1))
print_br(np.var(arr))

print_line("返回每行/列/所有数据的 std")
print_br(np.std(arr, axis=0))
print_br(np.std(arr, axis=1))
print_br(np.std(arr))
