# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 上午10:09
# @Author  : yidxue
import numpy as np
from dtaidistance import dtw
from dtaidistance import dtw_visualisation as dtwvis

s1 = np.array([1, 2, 0, 1, 1, 2, 0, 1, 1, 2, 0, 1, 1, 2, 0, 1])
s2 = np.array([0, 1, 1, 2, 0, 1, 1, 2, 0, 1, 1, 2, 0, 1, 1, 2])
s3 = np.array([0.8, 1.5, 0, 1.2, 0, 0, 0.6, 1, 1.2, 0, 0, 1, 0.2, 2.4, 0.5, 0.4])

d, paths = dtw.warping_paths(s1, s2)
print(d)
# print(paths)
print("=" * 40)
d, paths = dtw.warping_paths(s1, s3)
print(d)
# print(paths)
