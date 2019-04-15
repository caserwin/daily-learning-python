#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-19 15:18
# @Author  : erwin
import pandas as pd
from pandasd.function.util_function import *

df1 = pd.DataFrame(data={'name': ['a', 'b', 'c', 'd'], 'gender': ['male', 'male', 'female', 'female']})
df2 = pd.DataFrame(data={'name': ['a', 'b', 'c', 'e'], 'age': [21, 22, 23, 20]})

# 字段求差集
ds1 = set([tuple(line) for line in df1[['name']].values.tolist()])
ds2 = set([tuple(line) for line in df2[['name']].values.tolist()])
for d in ds1.difference(ds2):
    print_br(d)
