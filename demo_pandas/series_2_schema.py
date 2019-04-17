#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-17 10:41
# @Author  : erwin
import pandas as pd
from demo_pandas.function.util_function import *

data_dict_series = {
    '1490707920': 10,
    '1490708040': 20,
    '1490708200': None,
    '1490708100': 20,
}
pds = pd.Series(data_dict_series, name='test')

print_line("基本属性")
print_br(pds.index)
print_br(pds.name)
print_br(pds.values)
print_br(pds.dtype)