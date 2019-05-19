# -*- coding: utf-8 -*-
# @Time    : 2018/7/28 下午3:57
# @Author  : yidxue
import profile


def factorial(i: int):
    if i == 1:
        return i
    else:
        b = i - 1
        return i * factorial(b)


print(factorial(15))
profile.run("factorial(15)")
