# -*- coding: utf-8 -*-
# @Time    : 2018/8/12 上午11:50
# @Author  : yidxue
# 有序字典
import collections
import operator
from common.util_function import *

dic1 = collections.OrderedDict()
dic1['k1'] = 'v1'
dic1['k2'] = 'v2'
dic1['k3'] = 'v3'
print(dic1)

dic1 = collections.OrderedDict({"a": 2.11, "d": 3.5, "c": 1.4})
print(max(dic1.items(), key=operator.itemgetter(1))[0])

print_br("根据Key 排序")
print(sorted(dic1.items(), key=lambda kv: kv[0]))
print_br("根据value 排序")
print(sorted(dic1.items(), key=lambda kv: kv[1]))


class Person1(object):
    name = '1'
    age = 16


class Person2(object):
    cname = '2'
    cage = 32


dic = {"p1": Person1(), "p2": Person2()}
print(dic["p1"].age)
print(dic["p2"].cage)
print(dic["p1"].name)
print(dic["p2"].cname)

print(dic.get('p3', None))