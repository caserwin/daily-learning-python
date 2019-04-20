#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-20 18:31
# @Author  : erwin
import pandas as pd
from common.util_function import *

"""
类别类型可谓是非常常用的一种类型，其具有如下特征：
1. 取固定几种值；
2. 可以定义序，序的形式与实数序或字典序可以都不同；
3. 即使是数值表示，数值运算可能也无意义，与离散数值型不一定相同。

下面出现的参数 inplace =True 表示直接修改原数据，inplace = False 表示返回修改新数据，原数据不变
"""

print_line("类型:ordered=True 表示有序，False表示无序")
c = pd.Categorical(["1", "2", "3"], ordered=True)

print_line("原始数据、基本属性")
print_br(c)
print_br(c.categories)
print_br(c.ordered)

print_line("Category 增加类别值：add_categories")
c.add_categories(['4', '8'], inplace=True)
print_br(c)

print_line("Category 删除类别值：remove_categories")
c.remove_categories(['4'], inplace=True)
print_br(c)

print_line("Category 删除没有被用到的类别值：remove_unused_categories")
c.remove_unused_categories(inplace=True)
print_br(c)

print_line("Category 修改类别值：直接修改 或 rename_categories")
c.categories = ['3', '2', '6']
print_br(c)
c.rename_categories(['5', '6', '7'], inplace=True)
print_br(c)

print_line("Category 修改是否有序")
c.as_unordered(inplace=True)
print_br(c)
c.as_ordered(inplace=True)
print_br(c)

print_line("Category 修改 Category 值的顺序：reorder_categories")
# new_categories 不能新增Category值，不能修改Category值类型
c.reorder_categories(new_categories=['6', '7', '5'], ordered=True, inplace=True)
print_br(c)

print_line("Category 修改: set_categories，把原来别类全删了，设置新类别")
c.set_categories(new_categories=['6', '7', '8'], ordered=True, inplace=True)
print_br(c)

print_line("Category 查询：可以采用[]来查看，不支持loc[]和iloc[]方式")
print_br(c[0:2])
print_br(c[[True, False, True]])