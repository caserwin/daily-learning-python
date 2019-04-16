#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-15 22:16
# @Author  : erwin
import pandas as pd
import numpy as np
from demo_pandas.function.util_function import *

raw_data = {'name': ['Jason', 'Molly', np.nan, np.nan, np.nan],
            'nationality': ['USA', 'USA', 'France', 'UK', 'UK'],
            'age': [42, 52, 36, 24, 70]}
df = pd.DataFrame(raw_data, columns=['name', 'nationality', 'age'])


print_line("循环遍历")
for index, row in df.iterrows():
    for col_name in df.columns:
        print(row[col_name])
    print()
