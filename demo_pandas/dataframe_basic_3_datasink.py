#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-15 10:57
# @Author  : erwin
import pandas as pd
import numpy as np
from common.util_function import *

'''
http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_csv.html
'''

print_line("将 DataFrame 直接写入 CSV 文件")
data = np.array([[1, 2, 3, 4],
                 [4, 5, 6, 8],
                 [2, 3, 5, 9]])

df = pd.DataFrame(data=data, index=['a', 'b', 'c'], columns=['A', 'B', 'C', 'D'])
df.to_csv("./data/dataframe_16_datasink.csv", sep=",", encoding="utf-8", index=False, header=False)
