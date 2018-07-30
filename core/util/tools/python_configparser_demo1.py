# -*- coding: utf-8 -*-
# @Time    : 2018/7/28 下午4:19
# @Author  : yidxue


import ConfigParser

cf = ConfigParser.ConfigParser()
cf.read("../conf/app.conf")
secs = cf.sections()
ks = cf.options("mysql")
kvs = cf.items("mysql")
kv = cf.get("mysql", "password")

print(secs)
print(ks)
print(kvs)
print(kv)
