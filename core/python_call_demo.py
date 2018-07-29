# -*- coding: utf-8 -*-
# @Time    : 2018/7/28 下午3:35
# @Author  : yidxue


class Person:
    def __call__(self, name, age):
        self.name = name
        self.age = age
        print(self.name, age)


p = Person()
p("yidxue", 27)
