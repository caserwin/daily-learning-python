# -*- coding: utf-8 -*-
# @Time    : 2018/8/1 下午1:50
# @Author  : yidxue

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b'hello,this is a test info !', ('localhost', 8081))
print(s.recv(1024))
