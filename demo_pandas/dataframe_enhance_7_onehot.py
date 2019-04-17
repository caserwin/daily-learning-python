#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-16 15:23
# @Author  : erwin
import pandas as pd
from common.util_function import *

df = pd.DataFrame({'column1': ['aa', 'bb', 'cc'], 'column2': ['dd', 'ee', 'ff']})

print_line("原始数据")
print_br(df)

print_line("column1 one hot 编码")
dummy_df_column1 = pd.get_dummies(df.column1)
print_br(dummy_df_column1)

print_line("column2 one hot 编码")
dummy_df_column2 = pd.get_dummies(df.column2)
print_br(dummy_df_column2)

print_line("拼接")
df_res = pd.concat([dummy_df_column1, dummy_df_column2], axis=1)
print_br(df_res)
