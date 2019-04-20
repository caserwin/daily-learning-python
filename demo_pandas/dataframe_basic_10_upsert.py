#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-15 10:38
# @Author  : erwin
import pandas as pd
import numpy as np
from common.util_function import *

raw_data = {'name': ['Jason', 'Molly', np.nan, np.nan, np.nan],
            'nationality': ['USA', 'USA', 'France', 'UK', 'UK'],
            'age': [42, 52, 36, 24, 70]}
df = pd.DataFrame(raw_data, columns=['name', 'nationality', 'age'])

print_line("update 示例：把 name 不等于 null的 user 的age设置为 10")
df.loc[(df.name.notnull()), 'age'] = 10
print_br(df)

print_line("update 示例：把 nationality = USA 的 user 的age设置为 10")
df.loc[(df.nationality == 'UK'), 'age'] = 10
print_br(df)

print_line("replace 示例")
print_br(df.replace('USA', 'USA1'))
print_br(df.replace(['USA', 'UK'], ['USA1', 'UK1']))  # 分别替换
print_br(df.replace(['USA', 'UK'], 'Other'))  # 分别替换
print_br(df.nationality.replace('USA', 'USA1'))

print_line("增加一行")
df.loc[99] = [7, 8, 9]
print_br(df)

print_line("[] 增加一列")
df['H'] = [1, 2] * 3
print_br(df)

print_line("insert 增加一列")
col_f = [1, 2] * 3
df.insert(2, 'F', col_f)
print_br(df)

print_line("append 增加多行")
df1 = pd.DataFrame([[1, 2, 3], [1, 2, 3]], columns=['name', 'nationality', 'age'])
print_br(df.append(df1, ignore_index=True, sort=True))  # ignore_index=False表示使用原index
