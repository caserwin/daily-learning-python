#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-15 17:10
# @Author  : erwin
import numpy as np
import pandas as pd
from demo_pandas.function.util_function import *


def multiply(x):
    return x * 2


raw_data = {'name': ['Jason', 'Molly', np.nan, np.nan, np.nan],
            'nationality': ['USA', 'USA', 'France', 'UK', 'UK'],
            'age': [42, 52, 36, 24, 70]}
df = pd.DataFrame(raw_data, columns=['name', 'nationality', 'age'])

print_br(df["age"].apply(lambda age: 2 * age))
print_br(df["age"].apply(multiply))


