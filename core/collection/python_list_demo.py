# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 上午11:59
# @Author  : yidxue

print("=" * 40 + "生成list" + "=" * 40)
# 基于map方式，生成一个list
dic = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print(map(lambda item: item[1], dic.items()))

# 基于列表推导生成list。即根据一份列表制作另一份列表。
ls = [1, 2, 3, 4, 5]
print([x ** 2 for x in ls])
# 基于列表推导生成list。并且进行条件过滤
print([w for w in ['xyd', 'hyz', 'ssss', 'ewde'] if len(w) < 4])

print("=" * 40 + "list添加元素" + "=" * 40)
# 增加元素
ls.append("f")
print(ls)
# 在 list 中插入元素，并指定索引号。
ls.insert(2, 'xyd')
print(ls)
# 添加多个元素
ls.extend([1, 2, 3, 4])
print(ls)

print("=" * 40 + "list删除元素" + "=" * 40)
# 删除最后一个元素
print(ls.pop())
print(ls)

print("=" * 40)
# list中内容重复2遍
print(ls * 2)

print("=" * 40)
# python 对list进行去重，但是结果会乱序
ids = list(set(ls * 2))
print("去重后:" + ','.join(map(lambda x: str(x), ids)))

print("=" * 40)
# 关于list切片操作
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

print("=" * 40)
# 其他操作
ls = ['the', 'the', 'thw', 'tie', 'ahe']
print(ls.index('the'))  # 找出一个词第一次出现的索引号。
print(ls.count('the'))  # 统计某一个元素出现的次数
