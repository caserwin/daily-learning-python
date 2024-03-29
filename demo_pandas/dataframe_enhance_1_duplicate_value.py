#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-15 22:20
# @Author  : erwin
import pandas as pd
from common.util_function import *
import numpy as np

df = pd.DataFrame({'col1': ['a'] * 2 + ['b'] * 3, 'col2': [1, 1, 2, 3, 3]})

print_line("原始数据")
print_br(df)

print_line("duplicated()和drop_duplicates()方法默认判断全部列")
print_br(df.duplicated())
print_br(df.drop_duplicates())

print_line("指定列的集合判断是否重复")
print_br(df.duplicated(['col1']))
print_br(df.drop_duplicates(['col1']))

print_line("删除index 重复的数据")
data = np.array([[1, 2, 3, 4],
                 [4, 5, 6, 8],
                 [2, 3, 5, 9]])
df = pd.DataFrame(data=data, index=['a', 'a', 'b'], columns=['A', 'B', 'C', 'D'])
print_br(df)
print_br(df[~df.index.duplicated()])
