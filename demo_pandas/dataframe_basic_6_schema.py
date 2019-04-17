# -*- coding: utf-8 -*-
# @Time    : 2018/10/3 下午2:36
# @Author  : yidxue
import pandas as pd
from common.util_function import *

df = pd.DataFrame({"A": [1, 2, 3],
                   "B": [4, 5, 6],
                   "C": [4, 5, 6]})
print_line("原始数据")
print_br(df)
print_br(df.dtypes)

print_line("字段重命名：dataframe.rename()")
print_br(df.rename(index=str, columns={"A": "a", "B": "b"}))

print_line("字段重命名")
df.columns = ['C', 'D', 'E']
print_br(df)

print_line("reindex")
print_br(df.reset_index())

print_line("输出字段名")
print_br(df.columns.values)

print_line("类型转换")
df['C'] = df['C'].astype(float)
pd.to_numeric(df["D"], errors='coerce')
df.E = df.E.astype(str)
print_br(df.dtypes)
