#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-15 18:21
# @Author  : erwin
import pandas as pd
import numpy as np
from demo_pandas.function.util_function import *

'''
缺失值处理
1. 采用均值/出现次数设置missing值。对于一列数字，要获取平均值。
2. 对于一列非数字，例如字符，要找到出现频率最高的字符赋值给missing值
3. 删除缺失值

http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.fillna.html
http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.dropna.html 

'''

raw_data = {'name': ['Jason', 'Molly', np.nan, np.nan, np.nan],
            'nationality': ['USA', 'USA', 'France', 'UK', np.nan],
            'age': [42, 52, 36, 24, np.nan],
            'none': [np.nan, np.nan, np.nan, np.nan, np.nan],
            }
df = pd.DataFrame(raw_data, columns=['name', 'nationality', 'age', 'none'])
print_line("原始数据")
print_br(df)

print_line("检查空值 NaN")
print_br(pd.isnull(df))
print_br(pd.isnull(df.name))

print_line("填充固定值")
print_br(df.fillna(value=5))
print_br(df.none.fillna(value=5))

print_line("填充均值/中位数/众数")
# inplace=True 表示在原来的 dataframe 上修改，inplace=False 表示返回新的 dataframe。
df_tmp = df['age'].fillna(df['age'].mean(), inplace=False)
print_br(df_tmp)
df_tmp = df['age'].fillna(df['age'].median(), inplace=False)
print_br(df_tmp)
df_tmp = df['nationality'].fillna(df['nationality'].mode()[0], inplace=False)
print_br(df_tmp)

print_line("删除全部为NaN值的行/列")
print_br(df.dropna(axis=0, how='all'))
print_br(df.dropna(axis=1, how='all'))

print_line("删除任一为NaN值的行/列")
df = df.drop('none', axis=1).drop(4, axis=0)
print_br(df)
print_br(df.dropna(axis=0, how='any'))
print_br(df.dropna(axis=1, how='any'))
