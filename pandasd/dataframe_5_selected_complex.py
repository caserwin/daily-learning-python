#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-15 10:12
# @Author  : erwin
import numpy as np
import pandas as pd
from pandasd.function.util_function import *

raw_data = {'name': ['Jason', 'Molly', np.nan, np.nan, np.nan],
            'nationality': ['USA', 'USA', 'France', 'UK', 'UK'],
            'age': [42, 52, 36, 24, 70]}
df = pd.DataFrame(raw_data, columns=['name', 'nationality', 'age'])

print_line("查询 nationality = 'USA'，年龄大于50")
american = df['nationality'] == "USA"
elderly = df['age'] > 50
print_br(df[american & elderly])

print_line("查询first_name非空，国家是USA")
print_br(df[df['name'].notnull() & (df['nationality'] == "USA")])

print_line("select in 语法")
print_br(df.nationality.isin(['USA', 'France']))
print_br(df[df.nationality.isin(['USA', 'France'])])
