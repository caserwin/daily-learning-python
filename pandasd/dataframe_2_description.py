# -*- coding: utf-8 -*-
# @Time    : 2018/10/3 下午2:36
# @Author  : yidxue
import pandas as pd
import numpy as np
from pandasd.function.util_function import *


raw_data = {'name': ['Jason', 'Molly', np.nan, np.nan, np.nan],
            'nationality': ['USA', 'USA', 'France', 'UK', 'UK'],
            'age': [42, 52, 36, 24, 70]}
df = pd.DataFrame(raw_data, columns=['name', 'nationality', 'age'])

print_line("原始数据")
print_br(df.describe(include='all'))

print_line("查看缺少值和数据类型")
print_br(df.info())

print_line("数据探索")
print_br('数据框行数和列数：' + str(df.shape))
print_br('数据框维度：' + str(df.ndim))
print_br('数据框中数据个数：' + str(df.size))
print_br('数据框行数：' + str(len(df)))
print_br('数据框列数：%.1f' % (df.size / len(df)))
print_br('数据框列数：' + str(df.size / len(df)))
print_br('数据框索引' + str(df.index.values))
print_br('数据框列名' + str(df.columns.values))
print_br('每列值类型' + str(df.dtypes))

print_line("查看前10列，后5行")
print_br(df.head(10))
print_br(df.tail(5))

print_line("查看指定字段的每个值个数分布情况")
print_br(df.name.value_counts())

print_line("输出字段名")
print_br(df.columns.values)

print_line("检查空值 NaN")
print_br(pd.isnull(df))
print_br(pd.isnull(df.name))
