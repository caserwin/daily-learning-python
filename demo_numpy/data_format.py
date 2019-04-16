# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 下午2:43
# @Author  : yidxue
import numpy as np


float_formatter = lambda x: "%.2f" % x
np.set_printoptions(formatter={'float_kind': float_formatter})
print(np.random.randn(5) * 10)
