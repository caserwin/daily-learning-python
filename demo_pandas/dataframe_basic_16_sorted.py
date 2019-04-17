#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-15 17:43
# @Author  : erwin
import numpy as np
import pandas as pd
from common.util_function import *

data = np.array([[1, 2, 3, 4],
                 [4, 5, 6, 8],
                 [2, 3, 5, 9]])
df = pd.DataFrame(data=data, index=[2, 1, 3], columns=['A', 'B', 'C', 'D'])

print_br(df)

print_line("value升序排序")
print_br(df.sort_values(by=['A'], ascending=True))
print_line("value降序排序")
print_br(df.sort_values(by=['A'], ascending=False))

print_line("index升序排序")
print_br(df.sort_index(axis=0, ascending=True))
print_line("index降序排序")
print_br(df.sort_index(axis=0, ascending=False))
