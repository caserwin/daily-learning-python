# -*- coding: utf-8 -*-
# @Time    : 2018/10/3 下午2:36
# @Author  : yidxue
import pandas as pd
import numpy as np

date_index = pd.date_range('20140729', periods=10)
df = pd.DataFrame(np.random.randn(10, 5), columns=['A', 'B', 'C', 'D', 'E'], index=date_index)

print(df.describe(include='all'))
print("=" * 20)

# 查看缺少值和数据类型
print(df.info())
print("=" * 20)

# 数据探索
print('数据框行数和列数：' + str(df.shape))
print('数据框维度：' + str(df.ndim))
print('数据框中数据个数：' + str(df.size))
print('数据框行数：' + str(len(df)))
print('数据框列数：%.1f' % (df.size / len(df)))
print('数据框列数：' + str(df.size / len(df)))
print('数据框索引' + str(df.index.values))
print('数据框列名' + str(df.columns.values))
print('每列值类型' + str(df.dtypes))
print("=" * 20)

# 查看前10列，后5行
print(df.head(10))
print(df.tail(5))
print("=" * 20)

# 查看指定字段的每个值个数分布情况
print(df.A.value_counts())
print("=" * 20)

# 输出字段名
print(df.columns.values)