#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-15 22:20
# @Author  : erwin
import pandas as pd
from demo_pandas.function.util_function import *

df = pd.DataFrame({'col1': ['a'] * 2 + ['b'] * 3, 'col2': [1, 1, 2, 3, 3]})

print_line("原始数据")
print_br(df)

print_line("duplicated()和drop_duplicates()方法默认判断全部列")
print_br(df.duplicated())
print_br(df.drop_duplicates())

print_line("指定列的集合判断是否重复")
print_br(df.duplicated(['col1']))
print_br(df.drop_duplicates(['col1']))
