# -*- coding: utf-8 -*-
# @Time    : 2018/10/3 下午2:36
# @Author  : yidxue
import pandas as pd
from common.util_function import *

data = [[1, 2, 3, 4],
        [4, 5, 6, 8],
        [2, 3, 5, 9]]
df = pd.DataFrame(data=data, index=['a', 'b', 'c'], columns=['A', 'B', 'C', 'D'])

print_line("[]使用示例：根据column name获取")
print_br(df['A'])  # 取出A列
print_br(df[['A', 'B']])  # 取出A，B两列
print_br(df[0:2])  # 取出前2行

print_line("loc 使用示例：loc根据index name和 column name 定位元素")
print_br(df.loc[['a', 'c'], ['A', 'B']])
print_br(df.loc['a':'c', ['A', 'B']])

print_line("iloc 使用示例：iloc 根据行数和列数的下标（index）来定位元素")
print_br("选取第2行，第2列元素：\n" + str(df.iloc[1, 1]))
print_br("选取第3行：\n" + str(df.iloc[2:3]))
print_br("选取第1,2行，第1列：\n" + str(df.iloc[0:2, 0]))
print_br("选取第1,2行，第1,3列：\n" + str(df.iloc[[0, 1], [0, 2]]))

print_line("返回对应的行为True，且列为’B'的DataFrame")
mask1 = [False, True, True]
print_br(df.loc[mask1, 'B'])

mask1 = [False, True, False]
mask2 = [True, False, True, True]
print_br(df.iloc[mask1, mask2])
