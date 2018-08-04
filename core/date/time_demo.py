# -*- coding: utf-8 -*-
# @Time    : 2018/8/4 下午12:56
# @Author  : yidxue
from time import ctime
from time import time

# 时间 time 包整理
print('系统当前时间' + str(ctime()))
start = time()
# 你的程序
print('程序运行了' + str(time() - start) + '秒')