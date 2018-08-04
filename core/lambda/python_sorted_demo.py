# -*- coding: utf-8 -*-
# @Time    : 2018/8/4 下午3:22
# @Author  : yidxue

# list中的排序
ls = [36, 5, 12, 9, 21]
ls.sort(reverse=True)
print(ls)


def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0


# 默认的sorted
print(sorted([36, 5, 12, 9, 21]))
print(sorted([36, 5, 12, 9, 21], reversed_cmp))
