# -*- coding: utf-8 -*-
# @Time    : 2018/10/3 下午2:36
# @Author  : yidxue
import pandas as pd
from pandasd.function.util_function import *

df1 = pd.DataFrame(data={'name': ['a', 'b', 'c', 'd'], 'gender': ['male', 'male', 'female', 'female']})
df2 = pd.DataFrame(data={'name': ['a', 'b', 'c', 'e'], 'age': [21, 22, 23, 20]})

print_line("inner join")
print_br(pd.merge(df1, df2, on=['name'], how='inner'))

print_line("inner join")
print_br(df1.merge(df2, how='inner', on=['name']))

print_line("left join")
print_br(pd.merge(df1, df2, on=['name'], how='left'))

print_line("outer join")
print_br(pd.merge(df1, df2, on=['name'], how='outer'))
