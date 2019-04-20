#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-18 17:35
# @Author  : erwin
import numpy as np
import pandas as pd
from common.util_function import *

'''
计算任意两列直接的统计量，返回以列索引为新行索引和列索引的DataFrame
'''

df = pd.DataFrame([[1, 2], [2, 0]], columns=['B', 'C'])

print_line("原始数据")
print_br(df)

print_line("协方差")
print_br(df.cov())

print_line("相关系数")
print_br(df.corr())
