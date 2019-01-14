# -*- coding: utf-8 -*-
# @Time    : 2018/10/3 下午2:36
# @Author  : yidxue
import pandas as pd
import numpy as np

# date_index = pd.date_range('20140729', periods=10)
# df = pd.DataFrame(np.random.randn(10, 5), columns=['A', 'B', 'C', 'D', 'E'], index=date_index)
#
# print(df.describe(include='all'))
# print(df.info())
#
# print('数据框行数和列数：' + str(df.shape))
# print('数据框维度：' + str(df.ndim))
# print('数据框中数据个数：' + str(df.size))
# print('数据框行数：' + str(len(df)))
# print('数据框列数：%.1f' % (df.size / len(df)))
# print('数据框列数：' + str(df.size / len(df)))
# print('数据框索引' + str(df.index.values))
# print('数据框列名' + str(df.columns.values))
# print('每列值类型' + str(df.dtypes))

# print(df.head(10))
# print(df.tail(5))
# print(df.A.value_counts())
#
# df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
# print(df.rename(index=str, columns={"A": "a", "B": "c"}))
#
# # 数据框中，选取Cabin列中不为空的位置替换为“Yes”
# df.loc[(df.Cabin.notnull()), 'Cabin'] = "Yes"
#
# print(df.loc[:, [0, 1, 2, 3]])
# print(df.loc[1:2, 0:3])
# print(df.loc[1, 3])
# print(df.loc[0:100, ['Coupon_id', 'Date']])
#
# data = [[1, 2, 3, 4],
#         [4, 5, 6, 8],
#         [2, 3, 5, 9]]
# index = ['a', 'b', 'c']
# columns = ['A', 'B', 'C', 'D']
# df = pd.DataFrame(data=data, index=index, columns=columns)
# # “:”表示范围，[]表示切片操作
# print(df.loc[['a', 'c'], ['A', 'B']])
# print(df.loc['a':'c', ['A', 'B']])
# # 返回对应的行为True，且列为’B'的DataFrame
# mask1 = [False, True, False]
# print(df.loc[mask1, 'B'])

# print('选取第一行，第一列元素\n' + str(df.iloc[1, 1]))
# print(df.iloc[0:2, 0])
# print('选取第2行\n' + str(df.iloc[2:3]))
# print(df.iloc[[0, 1], [0, 2]])
#
# mask1 = [False, True, False]
# mask2 = [True, False]
# print(df.iloc[mask1, mask2])

# raw_data = {'first_name': ['Jason', 'Molly', np.nan, np.nan, np.nan],
#             'nationality': ['USA', 'USA', 'France', 'UK', 'UK'],
#             'age': [42, 52, 36, 24, 70]}
# df = pd.DataFrame(raw_data, columns=['first_name', 'nationality', 'age'])
#
# american = df['nationality'] == "USA"
# elderly = df['age'] > 50
#
# print(df[american & elderly])
# print(df[df['first_name'].notnull() & (df['nationality'] == "USA")])

df = pd.DataFrame({'columns1': ['a', 'b', 'c'], 'columns2': ['c', 'd', 'e']})
print(df)

print(df.columns1.isin(['a', 'b']))
print(df.columns1[df.columns1.isin(['a', 'b'])] == 'c')


pd.read_json('/Users/steviechen1982/Documents/GitHub/mng20days_B.json')