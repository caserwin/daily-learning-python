# -*- coding: utf-8 -*-
# @Time    : 2018/7/28 下午3:36
# @Author  : yidxue


class A(object):
    def __init__(self):
        self.name = 'dicts: yidxue'
        # self.age = 'dicts: 27'

    def __getattr__(self, item):
        if item == 'name':
            return 'getattr: yidxue'
        if item == 'age':
            return 'getattr: 27'


a = A()
print(a.name)  # 从__dict__里获得的
print(a.age)  # 从__getattr__获得的
