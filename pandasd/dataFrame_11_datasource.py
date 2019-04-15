#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-15 10:57
# @Author  : erwin
import pandas as pd
from pandasd.function.util_function import *

print_line("读取 CSV 格式的数据集")
print_br(pd.read_json('./data/test.json'))

print_line("读取 Excel 数据集")
"""
pd.read_excel("excel_file")
"""