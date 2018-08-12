# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 上午11:59
# @Author  : yidxue

print("=" * 40)
ls = [1, 2, 3]
print(ls)

# 基于map方式，生成一个list
dic = {"a": 1, "b": 2, "c": 3, "d": 4}
print(map(lambda item: item[1], dic.items()))

# 基于列表推导生成list。即根据一份列表制作另一份列表。
print([x ** 2 for x in ls])
# 基于列表推导生成list。并且进行条件过滤
print([w for w in ['xyd', 'hyz', 'ssss'] if len(w) < 4])

print("=" * 40)
# 增加元素
ls = [1, 2, 3]
ls.append(4)
print(ls)

# 在 list 中插入元素，并指定索引号。
ls.insert(2, 5)
print(ls)

# 添加多个元素
print(ls + [5, 6])  # 需要赋值给一个新的变量
ls.extend([7, 8])
print(ls)

# 改
ls[0] = 10
print(ls)

# 删除
print("删除最后一个元素：" + str(ls.pop()))
print(ls)
# 删除下标为1的元素
del ls[1]
print(ls)

print("=" * 40)
ls = ['a', 'b', 'c', 'd', 'e']
for i in ls:
    print(i)

#  enumerate 用法
for i, s in enumerate(ls):
    print("index: " + str(i) + "--> value: " + s + "--> value: " + ls[i])

# 两个集合同时遍历。当参数长度不同时，zip会以最短序列的长度为准来截断所得到的的元组。
ls1 = [1, 2, 3]
for (x, y) in zip(ls1, ls):
    print(str(x) + '->' + y)

print("=" * 40)
# list中内容重复2遍
ls = [1, 2, 3] * 2
print(ls)

# 输出成字符串
print("输出成字符串" + ','.join(str(n) for n in ls))

# 去重
ids = list(set(ls))
print(ids)
print("去重后：" + ','.join(map(lambda x: str(x), ids)))

# 判断
print(3 in ls)

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

# 查找
ls = ['the', 'the', 'thw', 'tie', 'ahe']
print(ls.index('the'))  # 找出一个词第一次出现的索引号。
print(ls.count('the'))  # 统计某一个元素出现的次数
