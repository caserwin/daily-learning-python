#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-15 14:08
# @Author  : erwin
import pandas as pd
import numpy as np
from common.util_function import *

'''
1. del: 删除dataframe中指定的列，这个是直接影响当前的dataframe，注意 del是python中的内置语句，没有返回值。如：del df['a']
2. drop：不会影响原来的dataframe，dop方法会返回一个删除了指定列的新的dataframe
'''

raw_data = {'name': ['Jason', 'Molly', np.nan, np.nan, np.nan],
            'nationality': ['USA', 'USA', 'France', 'UK', np.nan],
            'age': [42, 52, 36, 24, np.nan],
            'none': [np.nan, np.nan, np.nan, np.nan, np.nan],
            }
df = pd.DataFrame(raw_data, columns=['name', 'nationality', 'age', 'none'])
print_line("原始数据")
print_br(df)

print_line("drop 删除指定一行/列")
print_br(df.drop(4, axis=0))
print_br(df.drop('none', axis=1))

print_line("drop 删除多行/列")
print_br(df.drop([0, 1], axis=0))
print_br(df.drop(['name', 'nationality'], axis=1))

print_line("del 删除列")
del df['name']
print_br(df)
