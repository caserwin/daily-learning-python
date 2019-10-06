#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-15 20:28
# @Author  : erwin
import numpy as np
import pandas as pd

from common.util_function import *

np.random.seed(1)

df = pd.DataFrame(np.random.rand(8, 4), columns=list('ABCD'))
df['group'] = [0, 0, 1, 1, 0, 0, 1, 1]
# df['group2'] = [0, 0, 0, 0, 1, 1, 1, 1]

print_line("原始数据")
print_br(df)

print_line("聚合示例1 -- groupby() 传入一个字段名")
print_br(df.groupby('group').sum())
# print_br(df.groupby(['group', 'group2']).sum())
print_br(df.groupby('group').count())  # 等价于 df.A.value_counts()

print_line("聚合示例2 -- groupby() 传入一个字典")

func = lambda x: x.max() - x.min()
func.__name__ = 'Max - Min'

res_df = df.groupby(['group']).agg({'A': ['sum', 'max'],
                                    'B': 'mean',
                                    'C': 'sum',
                                    'D': func})

print_br(res_df)

print_line("分组统计 -- groupby() 也可以传入一个序列")
df["E"] = pd.cut(df.A, 3)
print(df)

print("========")
grouped = df.A.groupby(df["E"]).count()
print(grouped)
