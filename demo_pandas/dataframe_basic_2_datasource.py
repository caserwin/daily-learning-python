#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-15 10:57
# @Author  : erwin
import pandas as pd
from common.util_function import *

print_line("读取 CSV 格式的数据集")
print_br(pd.read_json('./data/test.json'))

print_line("读取 Excel 数据集")
df1 = pd.read_excel("excel_file")
df2 = pd.read_table('/Users/cisco/Desktop/1.txt', sep=' ', header=None, dtype=str, na_filter=False)
df3 = pd.read_csv('/Users/cisco/Desktop/2018-04-16.csv', sep="\t", header=None)
