#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-15 10:12
# @Author  : erwin
import numpy as np
import pandas as pd
from demo_pandas.function.util_function import *

'''
bool 类型的[]和loc[]都可以拿来用
'''

raw_data = {'name': ['Jason', 'Molly', np.nan, np.nan, np.nan],
            'nationality': ['USA', 'USA', 'France', 'UK', 'UK'],
            'age': [42, 52, 36, 24, 70]}
df = pd.DataFrame(raw_data, columns=['name', 'nationality', 'age'])

print_line("布尔索引：查询 nationality = 'USA'，年龄大于50")
american = df['nationality'] == "USA"
elderly = df['age'] > 50
print_br(df[american & elderly])
print_br(df.loc[american & elderly, ['name', 'age', 'nationality']])  # 相比[]+bool，loc + bool类型好处在于：还可以索引列

print_line("布尔索引：查询first_name非空，国家是USA")
print_br(df[df['name'].notnull() & (df['nationality'] == "USA")])

print_line("isin 语法")
print_br(df.nationality.isin(['USA', 'France']))
print_br(df[df.nationality.isin(['USA', 'France'])])

print_line("df.age[df.nationality.isin(['USA', 'France'])] == 42")
ts1 = df.nationality.isin(['USA', 'France'])
ts2 = df.age == 42
print_br(df[ts1 & ts2])
