#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/25 9:59 AM
# @Author : Erwin
import pandas as pd

df = pd.read_csv('/Users/yidxue/mygit/daily-learning-python/demo_pandas/data/user_click_count.csv', sep=",",
                 header=None)
df.columns = ['user', 'stat']

# 看分位数
print(df.describe(include='all'))

# 平均分组分组统计
quartiles = pd.cut(df.stat, 10)
grouped = df.stat.groupby(quartiles).count()
print(grouped)


# 自定义分组统计
def age_map_func(x):
    if 1 == x:
        return 1
    elif 2 <= x <= 3:
        return 2
    elif 4 <= x <= 10:
        return 3
    elif 10 < x:
        return 4


df.stat_map = df.stat.map(age_map_func)
print(df.stat_map.value_counts())

# 画图看结果
