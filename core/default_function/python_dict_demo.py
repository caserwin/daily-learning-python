# -*- coding: utf-8 -*-
# @Time    : 2018/7/28 下午3:36
# @Author  : yidxue


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("yidxue", 27)
print(p.__dict__)
print(p.__dict__['name'])
print(p.__dict__['age'])