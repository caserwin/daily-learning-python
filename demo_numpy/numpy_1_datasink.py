#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-17 15:18
# @Author  : erwin
import numpy as np
from demo_pandas.function.util_function import *

np.set_printoptions(precision=3)

arr = np.random.randint(5, size=(3, 4), dtype=int)
print_line("原始数据")
print_br(arr)

print_line("Writes to a text file")
np.savetxt('data/file.txt', arr, delimiter=' ')

print_line("Writes to a CSV file")
np.savetxt('data/file.csv', arr, delimiter=',')
