# -*- coding: utf-8 -*-
# @Time    : 2018/10/3 下午2:36
# @Author  : yidxue
import pandas as pd
from common.util_function import *

"""
http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html
http://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
"""

df1 = pd.DataFrame({'a': ['a', 'c', 'd'], 'b': [4, 6, 7]})
df2 = pd.DataFrame({'a': ['a', 'c', 'e'], 'c': [7, 9, 10]})

print_line("原始数据")
print_br(df1)
print_br(df2)

print_line("两个数据框基于行拼接")
df = pd.concat([df1, df2])
print_br(df)

print_line("两个数据框基于列拼接")
df = pd.concat([df1, df2], axis=1)
print_br(df)
