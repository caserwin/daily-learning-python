#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-16 16:47
# @Author  : erwin
import pandas as pd
from common.util_function import *

ser1 = pd.Series(range(4))
ser2 = pd.Series(range(3))
print_line("两个序列基于行拼接")
df = pd.concat([ser1, ser2])
print_br(df)

print_line("两个序列基于列拼接")
df = pd.concat([ser1, ser2], axis=1)
print_br(df)
