# -*- coding: utf-8 -*-
# @Time    : 2018/7/28 下午3:33
# @Author  : yidxue


class Person:
    def __new__(cls, name, age):
        print('__new__ called.')
        print(name, age)
        return super(Person, cls).__new__(cls)


p = Person("yidxue", 27)
