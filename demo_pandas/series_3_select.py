#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-16 16:47
# @Author  : erwin
import pandas as pd
from common.util_function import *

pds = pd.Series({
    '1490707920': 16.8219660272,
    '1490707980': 20.0681534509,
    '1490708040': 18.1842385903,
})

print_line("通过索引访问")
print_br(pds['1490707920'])

print_line("通过下标访问")
print_br(pds[0])

print_line("通过多个下标访问")
print_br(pds[[1, 2]])

print_line("bool 运算：select data where > 17")
print_br(pds[pds.values > 17])
