#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/6 11:27 AM
# @Author : Erwin
import pandas as pd
from common.util_function import *

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 100)

df = pd.read_csv('data/groupby-count-stat.csv', sep=",")
df["level"] = pd.cut(df.score, 20)

print_line("方法1")
# series 转 DataFrame
df_true = df[df["is_click"]].groupby("level").count()["account_id"].to_frame()
# rename 后必须赋予一个新的dataframe，才能生效
df_true = df_true.rename(columns={"account_id": "true_account_num"})

df_all = df.groupby("level").count()["account_id"].to_frame()
df_all = df_all.rename(columns={"account_id": "all_account_num"})

merge_df = pd.merge(df_true, df_all, on=['level'], how='outer')
merge_df['ratio'] = merge_df['true_account_num'] / merge_df['all_account_num']

print(merge_df)

print_line("方法2")
