#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-15 17:43
# @Author  : erwin
import numpy as np
import pandas as pd
from pandasd.function.util_function import *

data = np.array([[1, 2, 3, 4],
                 [4, 5, 6, 8],
                 [2, 3, 5, 9]])
df = pd.DataFrame(data=data, index=['a', 'b', 'c'], columns=['A', 'B', 'C', 'D'])

print_line("升序排序")
print_br(df.sort_values(by=['A'], ascending=True))
print_line("降序排序")
print_br(df.sort_values(by=['A'], ascending=False))
