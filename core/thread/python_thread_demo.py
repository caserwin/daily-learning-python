# -*- coding: utf-8 -*-
# @Time    : 2018/8/4 下午2:33
# @Author  : yidxue
import threading
from time import sleep

# 构建数据
ls = [i for i in range(10000)]
span = len(ls) / 10


# 单个线程执行
def my_print(ls, name):
    sleep(5)
    print(name + ":" + str(ls[0]))


# 多线程执行
for i in range(10):
    ls_new = ls[i * span:(i + 1) * span]
    t = threading.Thread(target=my_print, args=(ls_new, "线程:" + str(i),))
    t.start()
