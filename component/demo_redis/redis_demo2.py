#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/15 10:10 AM
# @Author : Erwin
from rediscluster import StrictRedisCluster

startup_nodes = [{"host": "10.xx.xx.xx", "port": "xxxx"}, {"host": "10.xx.xx.xx", "port": "xxxx"},
                 {"host": "10.xx.xx.xx", "port": "xxxx"}, {"host": "10.xx.xx.xx", "port": "xxxx"}]
rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
a = ["category_goods_recall_5798"]
for item in a:
    print(rc.get(item))
