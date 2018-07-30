# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 下午1:22
# @Author  : yidxue

# 两个集合同时遍历，zip比这个例子更一般化。当参数长度不同时，zip会以最短序列的长度为准来截断所得到的的元组。
ls1 = [1, 2, 3]
ls2 = [4, 5, 6]
for (x, y) in zip(ls1, ls2):
    print(x, '+', y, '=', x + y)

# 列表元素，进行字符串拼接
ls = [1, 5, 5, 3, 3, 4, 6]
s1 = ','.join(str(n) for n in ls)
print(s1)
