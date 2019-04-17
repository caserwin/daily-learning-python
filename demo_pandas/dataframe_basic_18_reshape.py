#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-15 20:30
# @Author  : erwin
import numpy as np
from common.util_function import *

print_line("使用reshape来更改数据的列数和行数")
ls = np.array([[1, 2, 3], [4, 5, 6]])
print_br(ls)
print_br(ls.reshape((3, 2)))
print_br(ls.reshape((6, -1)))
