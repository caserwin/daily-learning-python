#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-20 21:21
# @Author  : erwin
import pandas as pd

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 100)

titanic = pd.read_csv('./data/titanic.txt')
print(titanic.head())
