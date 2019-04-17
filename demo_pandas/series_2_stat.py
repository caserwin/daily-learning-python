#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-16 16:46
# @Author  : erwin
import pandas as pd
from common.util_function import *

data_dict_series = {
    '1490707920': 10,
    '1490708040': 20,
    '1490708200': None,
    '1490708100': 20,
}
pds = pd.Series(data_dict_series, name='test')

print_line("统计特性")
print_br(pds.var())
print_br(pds.mean())
print_br(pds.values)
print_br(pds.index)
print_br(pds.keys())
print_br(pds.dropna())
