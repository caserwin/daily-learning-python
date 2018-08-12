# -*- coding: utf-8 -*-
# @Time    : 2018/8/12 上午11:50
# @Author  : yidxue
# 有序字典
import collections

dic1 = collections.OrderedDict()
dic1['k1'] = 'v1'
dic1['k2'] = 'v2'
dic1['k3'] = 'v3'
print(dic1)

dic1 = collections.OrderedDict({"a": 1, "b": 2, "c": 3})
print(dic1)