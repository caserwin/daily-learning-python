# encoding: utf-8
# @Time    : 2018/7/29 下午1:00
# @Author  : yidxue

string = "hello world"
print('取最后一个字符 ' + string[-1])
print('统计o出现次数 ' + str(string.count('o')))
print('取倒数第4个到倒数第1个字符 ' + string[-4:-1])
print('hello world'.find('lo'))
print("=" * 40)
strs = '1203_2203_83.txt'
print(strs.rfind("—"))  # 从字符串末尾开始查找，第一个"_"位置, 如果找不到返回 -1
print(strs.rindex("_"))  # 从字符串末尾开始查找，第一个"_"位置, 如果找不到则抛出异常
print(strs.find("_"))  # 查找字符串出现的第一个"_"位置, 如果找不到返回 -1
print(strs.index("_"))  # 查找字符串出现的第一个"_"位置, 如果找不到则抛出异常
print("=" * 40)
# python split:  str.split(str="", num=string.count(str))
# str -- 分隔符
# num -- 分割次数

line = 'aa bb ccc  dddd'
print(line.split())  # 按一个空格或者多个空格分
print(line.split(' '))  # 按一个空格分
print(line.split(' ', 2))  # 按一个空格分，分两次

cols = "erwin"
tablename = "tableA"
sql = "SELECT {cols} FROM `{tablename}`".format(cols=cols, tablename=tablename)
print(sql)

print("=" * 40)
# 不设置指定位置，按默认顺序
print("{} {}".format("hello", "world"))
# 设置指定位置
print("{1} {0} {1}".format("hello", "world"))
# 设置关键字
print('{name},{age}'.format(age=18, name='kzc'))

ss = "123"
print('Features that have coeffcient of 0 are: %s' % ss)
