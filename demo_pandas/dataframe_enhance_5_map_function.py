#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-16 15:07
# @Author  : erwin
import numpy as np
import pandas as pd
from demo_pandas.function.util_function import *

'''
map ，Series 或 DataFrame列 都可以调用此方法。该方法接受一个函数或字典作为参数，应用于列的每一个元素，将元素值映射为另一个值。 多用于数据离散化。
'''


def age_map_func(x):
    if 0 <= x <= 30:
        return 1
    elif 31 <= x <= 50:
        return 2
    elif 51 < x:
        return 3


raw_data = {'name': ['Jason', 'Molly', np.nan, np.nan, np.nan],
            'nationality': ['USA', 'USA', 'France', 'UK', 'UK'],
            'age': [42, 52, 36, 24, 70]}
df = pd.DataFrame(raw_data, columns=['name', 'nationality', 'age'])

print_line("原始数据")
print_br(df)

print_line("function 映射：age 字段进行映射为[0,2]")
df['AGE_DIS'] = df.age.map(age_map_func)
print_br(df)

print_line("lambda 映射：age 字段进行映射为[0,2]")
df['AGE_LAMBDA'] = df['age'].map(lambda x: x + 1)
print_br(df)

print_line("dict 映射：age 字段进行映射为[0,2]")
df['nationality_DICT'] = df['nationality'].map({'USA': 0, 'France': 1, 'UK': 2})
print_br(df.head(10))
