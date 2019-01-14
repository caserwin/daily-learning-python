# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 上午11:37
# @Author  : yidxue
from dtaidistance import dtw
import array

s1 = [1, 2, 0, 1, 1, 2]
s2 = [1, 0, 1]
path = dtw.warping_path(s1, s2)
print(path)

s1 = [1, 2, 0, 1, 1, 2]
s2 = [1, 0]
distance, paths = dtw.warping_paths(s1, s2)
print(distance)

s1 = array.array('d', [1, 2, 0, 1, 1, 2])
s2 = array.array('d', [1, 0])
d = dtw.distance_fast(s1, s2)
print(d)
# print(paths)

# dtwvis.plot_warping(s1, s2, path, filename="warp.png")
# print(dtw.distance.__doc__)

print("=" * 20)

from dtaidistance import dtw
from dtaidistance import dtw_visualisation as dtwvis
import numpy as np

x = np.arange(0, 20, .5)
s1 = np.sin(x)
s2 = np.sin(x - 1)
d, paths = dtw.warping_paths(s1, s2, window=25, psi=1)
# d, paths = dtw.warping_paths(s1, s2)
best_path = dtw.best_path(paths)

print(d)
# print(paths)
print(best_path)

dtwvis.plot_warpingpaths(s1, s2, paths, best_path)
