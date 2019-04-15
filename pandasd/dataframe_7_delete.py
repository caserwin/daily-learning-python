#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-15 14:08
# @Author  : erwin
import pandas as pd
import numpy as np
from pandasd.function.util_function import *

raw_data = {'name': ['Jason', 'Molly', np.nan, np.nan, np.nan],
            'nationality': ['USA', 'USA', 'France', 'UK', np.nan],
            'age': [42, 52, 36, 24, np.nan],
            'none': [np.nan, np.nan, np.nan, np.nan, np.nan],
            }
df = pd.DataFrame(raw_data, columns=['name', 'nationality', 'age', 'none'])
print_line("原始数据")
print_br(df)

print_line("删除全部为NaN值的行/列")
print_br(df.dropna(axis=0, how='all'))
print_br(df.dropna(axis=1, how='all'))

print_line("删除指定一行/列")
print_br(df.drop(4, axis=0))
print_br(df.drop('none', axis=1))

print_line("删除任一为NaN值的行/列")
df = df.drop('none', axis=1).drop(4, axis=0)
print_br(df)
print_br(df.dropna(axis=0, how='any'))
print_br(df.dropna(axis=1, how='any'))
