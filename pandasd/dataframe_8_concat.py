# -*- coding: utf-8 -*-
# @Time    : 2018/10/3 下午2:36
# @Author  : yidxue
import pandas as pd

"""
http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html
http://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
"""

df1 = pd.DataFrame({'a': ['a', 'c', 'd'], 'b': [4, 6, 7]})
df2 = pd.DataFrame({'a': ['a', 'c', 'e'], 'c': [7, 9, 10]})

print(df1)
print(df2)

# 两个数据框基于行拼接
df = pd.concat([df1, df2])
print(df)
print()

# 两个数据框基于列拼接
df = pd.concat([df1, df2], axis=1)
print(df)
print()
