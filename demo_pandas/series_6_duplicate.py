#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-29 09:50
# @Author  : erwin
import pandas as pd
from common.util_function import *

s = pd.Series(range(4), index=["a", "a", "c", "d"])

print_line("删除index 重复的数据")
print_br(s)
print_br(s[~s.index.duplicated()])
