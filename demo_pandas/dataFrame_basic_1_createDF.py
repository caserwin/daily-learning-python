# -*- coding: utf-8 -*-
# @Time    : 2018/10/3 下午2:36
# @Author  : yidxue
import numpy as np
import pandas as pd
from common.util_function import *

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 100)

print_line("基于numpy 构建")
date_index = pd.date_range('20140729', periods=10, freq="5Min")
print_br(pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'], index=date_index))

print_line("基于list构建，其实这里也可以不需要 numpy.")
data = np.array([[1, 2, 3, 4],
                 [4, 5, 6, 8],
                 [2, 3, 5, 9]])
print_br(pd.DataFrame(data=data, index=['a', 'b', 'c'], columns=['A', 'B', 'C', 'D']))

print_line("基于列表-字典类型")
dic_ls = [{'col1': 'a', 'col2': '1'},
          {'col1': 'b', 'col2': '2'}]
print_br(pd.DataFrame(data=dic_ls))
print_br(pd.DataFrame.from_records(data=dic_ls))

print_line("基于字典-列表类型")
df = pd.DataFrame(data={'columns1': ['a', 'b', 'c'],
                        'columns2': ['c', 'd', 'e']})
print_br(df)

print_line("基于字典-字典类型")
data3 = {'A': {'a': 1, 'b': 4},
         'B': {'a': 2, 'b': 5},
         'C': {'a': 3, 'c': 6}}
df = pd.DataFrame(data=data3)
print_br(df)

print_line("基于json字符串")
print_br(pd.read_json("""[{"col1": "a", "col2": "1"}, {"col1": "b", "col2": "2"}]"""))
print_br(pd.read_json('./data/test.json'))
