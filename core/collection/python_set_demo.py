# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 下午12:00
# @Author  : yidxue

st = {'a', 'b', 'c'}
print(st)
print({x * 2 for x in st})
print({w for w in ['xyd', 'hyz', 'ssss'] if len(w) < 4})
st.add('d')
print(st)

print("=" * 40)
print('a' in st)
print('f' not in st)

print("=" * 40)
st1 = {'a', 'b', 'c'}
st2 = {'b', 'c', 'd'}
# 交集
print(st1 & st2)
# 差集
print(st1 - st2)
# 并集
print(st1 | st2)