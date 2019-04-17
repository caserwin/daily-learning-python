# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 下午12:02
# @Author  : yidxue
import numpy as np
from common.util_function import *

arr = np.array([(5, 2, 3), (4, 1, 6)])
print_line("元素数据")
print_br(arr)

print_line("最大值/最小值所在的位置")
print_br(np.argmin(arr))
print_br(np.argmax(arr))

print_line("矩阵转置")
print_br(arr.T)

print_line("把2维的矩阵转成1维的向量")
flatten_arr = arr.flatten()
print_br(flatten_arr)

print_line("reshape")
print_br(arr.reshape(3, 2))
