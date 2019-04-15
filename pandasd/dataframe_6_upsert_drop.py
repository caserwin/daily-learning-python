#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-15 10:38
# @Author  : erwin
import pandas as pd
import numpy as np

raw_data = {'name': ['Jason', 'Molly', np.nan, np.nan, np.nan],
            'nationality': ['USA', 'USA', 'France', 'UK', 'UK'],
            'age': [42, 52, 36, 24, 70]}
df = pd.DataFrame(raw_data, columns=['name', 'nationality', 'age'])

# update 示例
print("=" * 20 + "update示例" + "=" * 20)
# 把 name 不等于 null的 user 的age设置为 10
df.loc[(df.name.notnull()), 'age'] = 10
print(df)

# 把 nationality = USA 的 user 的age设置为 10
df.loc[(df.nationality == 'UK'), 'age'] = 10
print(df)


# update 示例

# 删除字段
print("=" * 20 + "删除示例" + "=" * 20)
print("删除列\n", df.drop('name', axis=1))
print("删除行\n", df.drop(1, axis=0))

