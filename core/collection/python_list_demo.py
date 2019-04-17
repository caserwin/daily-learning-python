# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 上午11:59
# @Author  : yidxue
from common.util_function import *

print_line("定义list")
ls = [1, 2, 3]
print_br(ls)

print_line("基于map方式，生成一个list")
dic = {"a": 1, "b": 2, "c": 3, "d": 4}
print(map(lambda item: item[1], dic.items()))

print_line("基于列表推导生成list。即根据一份列表制作另一份列表。")
print_br([x ** 2 for x in ls])
print_line("基于列表推导生成list。并且进行条件过滤")
print_br([w for w in ['xyd', 'hyz', 'ssss'] if len(w) < 4])

print_line("增加元素")
ls = [1, 2, 3]
ls.append(4)
print_br(ls)

print_line("在 list 中插入元素，并指定索引号。")
ls.insert(2, 5)
print_br(ls)

print_line("添加多个元素")
print_br(ls + [5, 6])  # 需要赋值给一个新的变量
ls.extend([7, 8])
print_br(ls)

print_line("改")
ls[0] = 10
print_br(ls)

print_line("删除")
print_br("删除最后一个元素：" + str(ls.pop()))
print_br(ls)
print_line("删除下标为1的元素")
del ls[1]
print_br(ls)

print_line("enumerate 用法")
ls = ['a', 'b', 'c', 'd', 'e']
for i, s in enumerate(ls):
    print_br("index: " + str(i) + "--> value: " + s + "--> value: " + ls[i])

print_line("两个集合同时遍历。当参数长度不同时，zip会以最短序列的长度为准来截断所得到的的元组。")
ls1 = [1, 2, 3]
for (x, y) in zip(ls1, ls):
    print_br(str(x) + '->' + y)

print_line("list中内容重复2遍")
ls = [1, 2, 3] * 2
print_br(ls)

print_line("输出成字符串")
print_br("输出成字符串" + ','.join(str(n) for n in ls))

print_line("去重")
ids = list(set(ls))
print_br(ids)
print_br("去重后：" + ','.join(map(lambda x: str(x), ids)))

print_line("判断是否存在")
print_br(3 in ls)

print_line("list切片操作")
ls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(ls[-1])  # h
print(ls[1])  # b
print(ls[:])  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(ls[:5])  # ['a', 'b', 'c', 'd', 'e']
print(ls[:-1])  # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(ls[4:])  # ['e', 'f', 'g', 'h']
print(ls[-3:])  # ['f', 'g', 'h']
print(ls[2:5])  # ['c', 'd', 'e']
print(ls[2:-1])  # ['c', 'd', 'e', 'f', 'g']
print(ls[-3:-1])  # ['f', 'g']

print_line("查找")
ls = ['the', 'the', 'thw', 'tie', 'ahe']
print_br(ls.index('the'))  # 找出一个词第一次出现的索引号。
print_br(ls.count('the'))  # 统计某一个元素出现的次数
