#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-15 22:25
# @Author  : erwin
import pandas as pd
import numpy as np
from demo_pandas.function.util_function import *

df = pd.DataFrame(np.random.randn(10, 4))

print_line("原始数据")
print(df)

print_line("筛选出异常值")
print(df[np.abs(df) > 1.5])

print_line("异常值处理")
df[np.abs(df) > 1.5] = '-'
print(df)

print_line("方法1：通过loc替换，把类别变量出现频率小于 2 的值归为 other")

raw_data = {'name': ['Jason', 'Molly', np.nan, np.nan, np.nan],
            'nationality': ['USA', 'USA', 'France', 'UK', 'UK'],
            'age': [42, 52, 36, 24, 70]}
df = pd.DataFrame(raw_data, columns=['name', 'nationality', 'age'])


def category_unify(category_field, threshold):
    field_count_dict = df[category_field].value_counts() < threshold
    index_field_dict = {}
    for index, field in df[category_field].iteritems():
        index_field_dict[index] = field_count_dict[field]
    return pd.Series(index_field_dict)


df.loc[category_unify('nationality', 2), 'nationality'] = "country"
print_br(df)
df.loc[category_unify('nationality', 2), 'name'] = "other"
print_br(df)

print_line("方法2：通过loc替换，把类别变量出现频率小于 2 的值归为 other")
df_dis_series = df.nationality.value_counts()
country_flag_series = df_dis_series < 2
for nationality, flag in country_flag_series.iteritems():
    if flag:
        df.nationality.replace(nationality, "country_2", inplace=True)
print_br(df)
