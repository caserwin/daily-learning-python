#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-15 20:48
# @Author  : erwin
import pandas as pd
import numpy as np
from demo_pandas.function.util_function import *

df = pd.DataFrame({'A': ['one', 'one', 'two'] * 4,
                   'B': ['A', 'B', 'C'] * 4,
                   'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D': np.random.randn(12),
                   'E': np.random.randn(12)})

print_line("原始数据")
print_br(df)

print_line("以C字段的值为列，以A/B字段的值为index，以 mean 方式聚合")
print_br(pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'], aggfunc='mean'))

print_line("以C字段的值为列，以A/B字段的值为index，以 sum 方式聚合")
print_br(pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'], aggfunc='sum'))

print_line("以C字段的值为列，以A/B字段的值为index，以 max 方式聚合")
print_br(pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'], aggfunc='max'))
