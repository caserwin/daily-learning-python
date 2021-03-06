# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 下午12:00
# @Author  : yidxue
import json
from common.util_function import *

print_line("定义一个词典")
dic1 = {"a": 1, "b": 2, "c": 3}
print(dic1)

print_line("生成一个字典")
values = {"a1", "b1", "c1"}
dic2 = dict(zip(values, range(len(values))))
print(dic2)

print_line("把序列的元素配对起来，但是如果参数长度不同，则字典长度为较短的序列的长度")
keys = ['spam', 'eggs', 'toast']
vals = [1, 3]
print(dict(zip(keys, vals)))

print_line("基于列表推导生成字典")
print({item[1]: item[0] for item in dic1.items()})

print_line("字典添加元素")
dic1 = {"a": 1, "b": 2, "c": 3}
dic1.setdefault('e', 5)
dic1["d"] = 4
print(dic1)

print_line("字典修改元素")
dic1["d"] = 42
print(dic1)

print_line("字典删除元素")
del dic1["d"]
dic1.pop("e")
print(dic1)

print_line("清空字典")
dic1.clear()
print(dic1)

print_line("对字典的遍历")
dic1 = {"a": 1, "b": 2, "c": 3}
for k in dic1.keys():
    print(k + "->" + str(dic1[k]))
for key, value in dic1.items():
    print(key + '->' + str(value))

print_line("获取字典元素")
print(dic1.get("a", "4"))
print(dic1.get("d", "4"))
print(dic1.keys())
print(dic1.values())
print(dic1.items())

print_line("判断字典中是否包含某一键")
print('a' in dic1.keys())

print_line("判断字典是否为空")
dict1 = {}
print(dict1 == {})

print_line("python 字符串和字典进行转化，方式1：")
a = '{"name":"yct","age":10}'
dic_a = eval(a)
print(dic_a)

print_line("python 字符串和字典进行转化，方式2：")
person = {"name": "yidxue", "age": 27}
person_str = json.dumps(person)
print(str(type(person_str)) + "\t" + person_str)
person_dic = json.loads(person_str)
print(str(type(person_dic)) + "\t" + str(person_dic))
