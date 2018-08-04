# -*- coding: utf-8 -*-
# @Time    : 2018/8/1 下午1:50
# @Author  : yidxue

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 从指定的端口，从任何发送者，接收UDP数据
s.bind(('localhost', 8081))
print('正在等待接入...')
while True:
    # 返回数据和客户端的地址&&端口
    data, addr = s.recvfrom(1024)
    print('Received:', data, 'from', addr)
    s.sendto('send back~', addr)
