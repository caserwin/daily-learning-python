# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 下午12:00
# @Author  : yidxue
import json

print("=" * 40)
# 定义一个词典
dic1 = {"a": 1, "b": 2, "c": 3}
print(dic1)

# 生成一个字典
values = {"a1", "b1", "c1"}
dic2 = dict(zip(values, range(len(values))))
print(dic2)

# 合并得到一个词典
dic = dict(dic1.items() + dic2.items())
print(dic)

# 把序列的元素配对起来，但是如果参数长度不同，则字典长度为较短的序列的长度
keys = ['spam', 'eggs', 'toast']
vals = [1, 3]
print(dict(zip(keys, vals)))

# 基于列表推导生成字典
dic_3 = {item[1]: item[0] for item in dic.items()}
print(dic_3)

print("=" * 40)
# 对字典的遍历
for k in dic.keys():
    print(k + "->" + str(dic[k]))
for key, value in dic.items():
    print(key + '->' + str(value))

# 返回字典元素
print(dic.keys())
print(dic.values())
print(dic.items())

print("=" * 40)
# 判断字典中是否包含某一键
print(dic.has_key('a'))
print('a' in dic.keys())

# # python 字符串和字典进行转化，方式1：
# a = '{"name":"yct","age":10}'
# dic_a = eval(a)
# print(dic_a)
#
# # python 字符串和字典进行转化，方式2：
# person = {"name": "yidxue", "age": 27}
# person_str = json.dumps(person)
# person_dic = json.loads(person_str)
# print(person_dic)
#
# # 判断字段是否为空
# dict1 = {}
# print(dict1 == {})
#
# # 有序字典
# import collections
#
# dic = collections.OrderedDict()
# dic['k1'] = 'v1'
# dic['k2'] = 'v2'
# dic['k3'] = 'v3'
# print(dic)
