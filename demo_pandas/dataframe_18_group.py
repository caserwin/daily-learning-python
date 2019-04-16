#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-15 20:28
# @Author  : erwin
import pandas as pd
import numpy as np
from demo_pandas.function.util_function import *

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                         'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three',
                         'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})
print_line("原始数据")
print_br(df)

print_line("聚合数据")
print_br(df.groupby('A').sum())
print_br(df.groupby(['A', 'B']).sum())
print_br(df.groupby('A').count())  # 等价于 df.A.value_counts()
