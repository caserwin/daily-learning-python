#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-15 17:37
# @Author  : erwin
import numpy as np
import pandas as pd
from common.util_function import *

data = np.array([[3, 2, 3, 4],
                 [2, 5, 6, 8],
                 [2, 3, 5, 9]])
df = pd.DataFrame(data=data, index=['a', 'b', 'c'], columns=['A', 'B', 'C', 'D'])

print_line("select unique")
print_br(df["D"].unique())

print_line("查看指定字段的每个值个数分布情况")
print_br(df.A.value_counts())

print_line("Sum of values in a data frame")
print_br(df.sum())
print_br(df.A.sum())

print_line("Lowest value of a data frame")
print_br(df.min())

print_line("Highest value")
print_br(df.max())

print_line("Index of the lowest value")
print_br(df.idxmin())

print_line("Index of the highest value")
print_br(df.idxmax())

print_line("Average values")
print_br(df.mean())

print_line("Median values")
print_br(df.median())

print_line("Correlation between columns")
print_br(df.corr())

print_line("To get these values for only one column, just select it like this")
print_br(df["A"].median())
