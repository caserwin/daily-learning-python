#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/6 11:01 AM
# @Author : Erwin
import matplotlib
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/yidxue/mygit/daily-learning-python/demo_pandas/data/correlation-coefficient.csv', sep=",",
                 header=None)
df.columns = ['p_id', 'user_count', 'gender_0', 'gender_1', 'gender_2', 'v_type_0', 'v_type_1', 'v_type_2',
              'v_type_3', 'history_click', 'action_score', 'click_percent', 'day']

df = df[df['user_count'] > 1000]
# print(df)

# print("gender_0 和 click_percent相关系数  ", df.gender_0.corr(df.click_percent))
# print("gender_1 和 click_percent相关系数  ", df.gender_1.corr(df.click_percent))
# print("gender_2 和 click_percent相关系数  ", df.gender_2.corr(df.click_percent))
#
# print("v_type_0 和 click_percent相关系数  ", df.vip_type_0.corr(df.click_percent))
# print("v_type_1 和 click_percent相关系数  ", df.vip_type_1.corr(df.click_percent))
# print("v_type_2 和 click_percent相关系数  ", df.vip_type_2.corr(df.click_percent))
# print("v_type_3 和 click_percent相关系数  ", df.vip_type_3.corr(df.click_percent))
#
# print("action_score 和 click_percent相关系数  ", df.action_score.corr(df.click_percent))
# print("history_click 和 click_percent相关系数  ", df.history_click.corr(df.click_percent))

print("history_click, action_score", (df.history_click + df.action_score).corr(df.click_percent))
print("history_click, action_score, v_type_1", (df.history_click + df.action_score + df.v_type_1).corr(df.click_percent))
print("history_click, action_score, v_type_1, v_type_2", (df.history_click + df.action_score + df.v_type_1 + df.v_type_2).corr(df.click_percent))

plt.scatter(df.history_click.tolist(), df.click_percent.tolist(), label='1')
plt.show()
