# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 下午1:38
# @Author  : yidxue

def my_function(num):
    if 5 < num < 10:
        return True


ls = [12, 50, 8, 17, 65, 14, 9, 6, 14, 5]
# demo 1
print(filter(my_function, ls))
# demo 2
print(filter(lambda num: True if 5 < num < 10 else False, ls))