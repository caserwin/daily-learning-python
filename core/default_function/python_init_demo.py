# -*- coding: utf-8 -*-
# @Time    : 2018/7/28 下午3:34
# @Author  : yidxue


class Person:
    def __new__(cls, name, age):
        print('__new__ called.')
        return super(Person, cls).__new__(cls)

    def __init__(self, name, age):
        print('__init__ called.')
        self.name = name
        self.age = age
        print(self.name, age)


p = Person("yidxue", 27)
