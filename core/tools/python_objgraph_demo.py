# -*- coding: utf-8 -*-
# @Time    : 2018/7/28 下午3:50
# @Author  : yidxue

x = [1, 2, 3]
y = [x, dict(key1=x)]
z = [y, (x, y)]

import objgraph
objgraph.show_refs([z], filename='ref_topo.png')