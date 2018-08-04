# -*- coding: utf-8 -*-

# 删除某个元素
a = [1, 2, 3, 4, 5]
b = [2, 2, 2, 0, 5]
print(a.pop())

# zip demo
print([i + j for i, j in zip(a, b)])

# 三目运算符 demo
print(True if 5 > 3 else False)

# 类型判断
dic = {"JOINMETHOD": {"ActiveX": "1", "Extension": {"USERTYPE": {"NEW": "1", "RETURN": "0"}}}}
print(isinstance(dic["JOINMETHOD"], dict))
print(isinstance([1, 2, 3], list))

# python 生成 10 - 20之间的随机小数
import random

print(random.uniform(10, 20))

# all() 函数使用示例，通常用于参数校验
print(all([0, 1, 2, 3, 4]))
print(all([1, 2, 3, ""]))
print(all([1, 2, 3, None]))
print(all([1, 2, 3, False]))
print(all([1, 2, 3, 4]))
