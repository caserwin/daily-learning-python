#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-20 19:21
# @Author  : erwin
import pandas as pd
from common.util_function import *

'''
Series 转为 Category
'''

s2c = pd.Series([1, 2, 3, 1]).astype('category')
print_line("Series 转 Category：但是相同的操作，要加上cat，如下：")
print_br(s2c)
print_br(s2c.cat.categories)
print_br(s2c.cat.ordered)

print_line("cut：用于将连续型变量分割为类别变量")
'''
cut(x, bins, right=True, labels=None, retbins=False, precision=3, include_lowest=False, duplicates='raise')
        
- x：待分割的Series或序列；
- bins：如果是int，那么将Series的进行等分，并在最大最小值的基础上外延1%作为区间边界；如果是序列，那么将序列值作为分隔点；
- right：True or False，分隔区间默认为左闭右开；
- labels：分隔后的类别标签
- retbins：是否返回分隔点；
- include_lowest：True or False，将最左侧区间的左值外延1%，试图去包含最小值；   
'''

s = pd.Series(range(0, 5))
print_br(s)
print_br(pd.cut(s, 3))
print_br(pd.cut(s, 3, labels=['a', 'b', 'c']))
print_br(pd.cut(s, 3, labels=['a', 'b', 'c'], retbins=True))
print_br(pd.cut(s, bins=[0, 2.5, 3.5, 4], labels=['a', 'b', 'c'], right=False))

print_line("qcut：用于将连续型变量分割为类别变量")
"""
- x：待分割的Series或序列；
- q：安装分位数也来定义分隔点，而不是按照给定值；
- labels：分隔后是区间，可以用label来替换为想要的类别形式；
- retbins：是否返回分隔点；
"""
print_br(s)
print_br(pd.qcut(s, q=[0.0, 0.25, 0.5, 0.75, 1.0], labels=['a', 'b', 'c', 'd']))
