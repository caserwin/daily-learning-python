#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-15 17:37
# @Author  : erwin
import numpy as np
import pandas as pd
from pandasd.function.util_function import *

data = np.array([[1, 2, 3, 4],
                 [4, 5, 6, 8],
                 [2, 3, 5, 9]])
df = pd.DataFrame(data=data, index=['a', 'b', 'c'], columns=['A', 'B', 'C', 'D'])

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
