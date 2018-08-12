# -*- coding: utf-8 -*-
# @Time    : 2018/8/12 下午3:24
# @Author  : yidxue


class person:
    name = "yidxue"


p = person()
print(hasattr(p, "age"))
print(getattr(p, "age", setattr(p, "age", "27")))  # age属性不存在时，设置该属性
print(getattr(p, "age"))  # 可检测设置成功
print(hasattr(p, "age"))  # True
print(p.name + " -> " + p.age)  # 27
