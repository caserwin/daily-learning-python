#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-15 22:25
# @Author  : erwin
import pandas as pd
import numpy as np
from demo_pandas.function.util_function import *

df = pd.DataFrame(np.random.randn(10, 4))

print_line("原始数据")
print(df)

print_line("筛选出异常值")
print(df[np.abs(df) > 1.5])

print_line("异常值处理")
df[np.abs(df) > 1.5] = '-'
print(df)
