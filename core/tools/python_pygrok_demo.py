# -*- coding: utf-8 -*-
# @Time    : 2018/8/5 上午9:23
# @Author  : yidxue
from pygrok import Grok

text = """221.215.155.234 - - [22/Dec/2016:08:00:00 +0800] "GET /js/scrollnav.js HTTP/1.1" 304 -"""
pattern = """%{IP:client_ip} - - [22/Dec/2016:08:00:00 +0800] "GET /js/scrollnav.js HTTP/1.1" 304 -"""
text_1 = """111.207.151.87 - - [2017-04-02 17:04:42 +0800] "GET /static/js/libs.kekxmhycgi.js/ HTTP/1.1" 505 5"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"""
pattern_1 = """%{IP:client_ip} - -"""
text_2 = 'gary is male, 25 years old and weighs 68.5 kilograms'
pattern_2 = '%{WORD:name} is %{WORD:gender}, %{NUMBER:age:int} years'
grok = Grok(pattern)
print(grok.match(text))
print('================================')
grok = Grok(pattern_1)
print(grok.match(text_1))
print('================================')
grok = Grok(pattern_2)
print(grok.match(text_2))
