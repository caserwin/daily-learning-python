#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-18 18:12
# @Author  : erwin
import numpy as np
import pandas as pd
from common.util_function import *

data = np.array([[1.22, 2.21, 3.31, 4.41],
                 [4, 5, 6, 8],
                 [2, 3, 5, 9]])
df = pd.DataFrame(data=data, index=['a', 'b', 'c'], columns=['A', 'B', 'C', 'D'])

print_line("round：修改精度")
print_br(df.round(1))

print_line("clip：原数据中小于lower 设为 lower，大于 upper 设为 upper")
print_br(df.clip(2, 4))

print_line("cumsim, cummin, cummax, cumprod：按行/列累计计算")
print_br(df.cumsum(axis=1))
print_br(df.cumsum(axis=0))
# print_br(df.A.cumsum(axis=1))
print_br(df.A.cumsum(axis=0))

