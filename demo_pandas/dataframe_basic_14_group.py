#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-15 20:28
# @Author  : erwin
import pandas as pd
import numpy as np
from common.util_function import *
from functools import reduce

np.random.seed(1)

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                         'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three',
                         'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})
print_line("原始数据")
print_br(df)

print_line("聚合示例1")
print_br(df.groupby('A').sum())
print_br(df.groupby(['A', 'B']).sum())
print_br(df.groupby('A').count())  # 等价于 df.A.value_counts()

print_line("聚合示例2")


def sum(series):
    return reduce(lambda x, y: x + y, series)


def sum_multi(s1, s2):
    count = 0
    for i, j in zip(s1, s2):
        count = count + i * j
    return count / len(s1)


res_df = df.groupby(['A']).agg({
    'C': sum,
    'D': sum,
})

print_br(res_df)

print_line("分组统计")
# import matplotlib.pyplot as plt

df1 = pd.DataFrame(data={'A': [1, 2, 2.5, 3, 5, 4, 3, 2, 1, 4],
                         'B': [2, 0, 2, 2, 0, 2, 2.5, 3, 5, 4]})
print(df1.head())
quartiles = pd.cut(df1.A, 3)
grouped = df1.A.groupby(quartiles).count()
print(grouped)