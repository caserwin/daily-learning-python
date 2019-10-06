#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-15 10:57
# @Author  : erwin
import pandas as pd
from common.util_function import *

'''
pd.read_csv(filepath, sep=',', header='infer', names=None,index_col=None, encoding=None )
    filepath：路径中不要带中文，容易报错。
    sep: csv文件数据的分隔符，默认是','，根据实际情况修改；
    header：如果有列名，那么这一项不用改；
    names：如果没有列名，那么必须设置header = None， names为列名的列表，不设置默认生成数值索引；
    index_col：int型，选取这一列作为索引。
    encoding：根据你的文档编码来确定，如果有中文读取报错，试试encoding = 'gbk'。


pd.read_excel(io, sheetname=0, header=0, index_col=None, names=None)
    header：如果有列名，那么这一项不用改；
    names：如果没有列名，那么必须设置header = None， names为列名的列表，不设置默认生成数值索引；
    index_col：int型，选取这一列作为索引。
'''

print_line("读取 CSV 格式的数据集")
print_br(pd.read_json('./data/test.json'))

print_line("读取 Excel 数据集")
df1 = pd.read_excel("excel_file")
df2 = pd.read_table('/Users/cisco/Desktop/1.txt', sep=' ', header=None, dtype=str, na_filter=False)
df3 = pd.read_csv('/Users/cisco/Desktop/2018-04-16.csv', sep="\t", header=None)
# df3.columns = ['C', 'D', 'E']

# pd.read_csv('./data/opentsdb_L.csv', sep = ',',index_col=0)  # 第1列作为 index.
