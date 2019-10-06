#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/6 11:27 AM
# @Author : Erwin
import pandas as pd


# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 100)

df = pd.read_csv('data/groupby-count-stat.csv', sep=",")
df["level"] = pd.cut(df.score, 20)

df_true = df[df["is_click"]].groupby("level").count()["account_id"].to_frame()
df_all = df.groupby("level").count()["account_id"].to_frame()

merge_df = pd.merge(df_true, df_all, on=['level'], how='outer')
merge_df['ratio'] = merge_df['account_id_x'] / merge_df['account_id_y']

print(merge_df)
