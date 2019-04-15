# -*- coding: utf-8 -*-
# @Time    : 2018/10/3 下午2:36
# @Author  : yidxue
import pandas as pd

data = [[1, 2, 3, 4],
        [4, 5, 6, 8],
        [2, 3, 5, 9]]
index = ['a', 'b', 'c']
columns = ['A', 'B', 'C', 'D']
df = pd.DataFrame(data=data, index=index, columns=columns)

# 返回对应的行为True，且列为’B'的DataFrame
mask1 = [False, True, True]
print(df.loc[mask1, 'B'])

mask1 = [False, True, False]
mask2 = [True, False, True, True]
print(df.iloc[mask1, mask2])
print("=" * 20)

# loc 使用示例
print(df.loc[['a', 'c'], ['A', 'B']])
print(df.loc['a':'c', ['A', 'B']])
print("=" * 20)

# iloc 使用示例
print("选取第2行，第2列元素：\n" + str(df.iloc[1, 1]))
print("选取第3行：\n" + str(df.iloc[2:3]))
print("选取第1,2行，第1列：\n" + str(df.iloc[0:2, 0]))
print("选取第1,2行，第1,3列：\n" + str(df.iloc[[0, 1], [0, 2]]))
print("=" * 20)
