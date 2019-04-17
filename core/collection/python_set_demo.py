# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 下午12:00
# @Author  : yidxue
from common.util_function import *

st = {'a', 'b', 'c'}
print_br(st)

st1 = {'b', 'c', 'd', 'e'}
st.update(st1)
print_br(st1)
print_br(st)

print_br({x * 2 for x in st})
print_br({w for w in ['xyd', 'hyz', 'ssss'] if len(w) < 4})
st.add('d')
print_br(st)

print_line("判断是否存在")
print_br('a' in st)
print_br('f' not in st)


print_line("交集")
st1 = {'a', 'b', 'c'}
st2 = {'b', 'c', 'd'}

print_br(st1 & st2)
print_br(st1.intersection(st2))

print_line("差集")
print_br(st1 - st2)

print_line("并集")
print_br(st1 | st2)
