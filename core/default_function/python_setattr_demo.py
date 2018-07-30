# -*- coding: utf-8 -*-
# @Time    : 2018/7/28 下午3:37
# @Author  : yidxue


class A(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setattr__(self, *args, **kwargs):
        print("call setattr")
        return object.__setattr__(self, *args, **kwargs)


a = A("yidxue", 27)
a.gender = 'male'  # 相当于调用了：a.__setattr__('gender', 'male')
print(a.__dict__)
