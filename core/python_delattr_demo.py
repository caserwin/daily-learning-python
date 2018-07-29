# -*- coding: utf-8 -*-
# @Time    : 2018/7/28 下午3:38
# @Author  : yidxue


class A(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __delattr__(self, *args, **kwargs):
        print('call func del attr')
        return object.__delattr__(self, *args, **kwargs)


a = A("yidxue", 27)
print(a.__dict__)
del a.name
print(a.__dict__)
