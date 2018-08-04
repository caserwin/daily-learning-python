# -*- coding: utf-8 -*-
# @Time    : 2018/8/3 下午12:38
# @Author  : yidxue
import re

text = "erwin 222 rrr 888 ..."
# match 正则匹配，使用示例
print(re.match(r"\w+", text).group())
# print(re.match(r"\d+", text).group())           # 运行报错
# match 正则捕获，使用示例
m = re.match(r'(\d{3})-(\d{3,8})$', '010-12345')  # 必须从第一个字符开始匹配
print(m.groups())

print("=" * 40)
# search 正则匹配，使用示例
print(re.search(r"\w+", text).group())
print(re.search(r"\d+", text).group())

# search 正则捕获，使用示例
m = re.search(r'(\d{3})-(\d{3,8})$', 'w010-12345')  # 无需从第一个字符开始匹配
print(m.groups())

print("=" * 40)
# findall 正则匹配，使用示例
regex = re.compile(r'\d+')
matchObj = regex.findall("erwin 222 rrr 888 ...")
print(','.join(matchObj))
# findall 正则捕获，使用示例
print(','.join(re.findall(r"a(\d+?)b", "a123ba234b")))
print(','.join(re.findall(r'\w*oo\w*', "wood am tool, sad toor")))

print("=" * 40)
# 正则切割字符串
string = 'dd ddd  fff a'
print(re.split('\s+', string))
print(re.split('  | ', string))  # 逻辑或

# re.sub使用示例
p = re.compile('dog')
print(p.sub('cat', 'I have a dog , you have a dog , he have a dog'))
print(p.sub('cat', 'I have a dog , you have a dog , he have a dog', 2))
print(re.sub(r'dog', 'cat', 'I have a dog , you have a dog , he have a dog'))
print(re.sub(r'dog', 'cat', 'I have a dog , you have a dog , he have a dog', 2))


def dashrepl(matchobj):
    if matchobj.group(0) == '-':
        return ' '
    else:
        return '~'


print(re.sub('-{1,2}', dashrepl, 'pro-gram--files'))
print(re.sub('-{1,2}', lambda x: ' ' if x.group(0) == '-' else '~', 'pro-gram--files'))
