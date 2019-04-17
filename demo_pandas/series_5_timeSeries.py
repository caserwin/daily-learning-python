#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-15 21:12
# @Author  : erwin
import pandas as pd
import numpy as np
from common.util_function import *

rng = pd.date_range('1/1/2012', periods=100, freq='S')
ts = pd.Series(np.random.randint(0, 10, len(rng)), index=rng)

print_line("原始数据")
print_br(ts)

print_line("聚合数据")
print_br(ts.resample('1Min').sum())
print_br(ts.resample('1Min').mean())
