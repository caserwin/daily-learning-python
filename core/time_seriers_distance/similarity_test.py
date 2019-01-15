# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 上午11:37
# @Author  : yidxue
# from dtaidistance import dtw
# import array
#
# s1 = [1, 2, 0, 1, 1, 2]
# s2 = [1, 0, 1]
# path = dtw.warping_path(s1, s2)
# print(path)
#
# s1 = [1, 2, 0, 1, 1, 2]
# s2 = [1, 0]
# distance, paths = dtw.warping_paths(s1, s2)
# print(distance)
#
# s1 = array.array('d', [1, 2, 0, 1, 1, 2])
# s2 = array.array('d', [1, 0])
# d = dtw.distance_fast(s1, s2)
# print(d)
# # print(paths)
#
# # dtwvis.plot_warping(s1, s2, path, filename="warp.png")
# # print(dtw.distance.__doc__)

import numpy as np
import matplotlib.pyplot as plt
from dtaidistance import dtw
from core.similarity.cos_similar import CosSimilarity
from core.similarity.pearson_similar import PearsonSimilarity
from core.similarity.time_series_similar import TimeSeriesSimilarity

x = np.arange(0, 20, .5)
s1 = np.sin(x)
s2 = np.sin(x - 2)
d, paths = dtw.warping_paths(s1, s2)

plt.figure()
plt.plot(x, s1)
plt.plot(x, s2)
plt.show()

# 距离
# 1. 欧氏距离
dist = np.sqrt(np.sum(np.square(s1 - s2)))
print(dist)
# 2. 时间序列距离
print(d)
# 3. 时间序列距离
print(TimeSeriesSimilarity(s1, s2)[0])

print("=" * 40)
# 相似度
# 1. 余弦相似
print(CosSimilarity(s1, s2))
# 2. person相似
print(PearsonSimilarity(s1, s2))
# 3. 时间序列相似度
print(1 / (1 + d))
