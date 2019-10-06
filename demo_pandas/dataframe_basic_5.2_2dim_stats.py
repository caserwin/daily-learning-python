#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-18 17:35
# @Author  : erwin
import pandas as pd

from common.util_function import *

'''
计算任意两列直接的统计量，返回以列索引为新行索引和列索引的DataFrame
'''

df = pd.DataFrame([[1, 2], [2, 0]], columns=['B', 'C'])

print_line("原始数据")
print_br(df)

print_line("协方差")
print_br(df.cov())

print_line("相关系数")
print_br(df.corr())

print_line("分组统计")
# import matplotlib.pyplot as plt

df1 = pd.DataFrame(data={'A': [1, 2, 2.5, 3, 5, 4, 3, 2, 1, 4],
                         'B': [2, 0, 2, 2, 0, 2, 2.5, 3, 5, 4]})
print(df1.head())
quartiles = pd.cut(df1.A, 3)
grouped = df1.A.groupby(quartiles).count()
print(grouped)
# grouped.plot()
