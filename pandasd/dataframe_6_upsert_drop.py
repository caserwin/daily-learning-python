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


# 把 name 不等于 null的 user 的age设置为 10
df.loc[(df.name.notnull()), 'age'] = 10
print(df)

# 把 nationality = USA 的 user 的age设置为 10
df.loc[(df.nationality == 'UK'), 'age'] = 10
print(df)