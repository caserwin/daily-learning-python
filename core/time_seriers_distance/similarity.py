# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 上午10:39
# @Author  : yidxue
import numpy as np

float_formatter = lambda x: "%.2f" % x
np.set_printoptions(formatter={'float_kind': float_formatter})


def warping_paths(s1, s2, **_kwargs):
    l1 = len(s1)
    l2 = len(s2)
    window = max(l1, l2)
    paths = np.full((l1 + 1, l2 + 1), np.inf)
    paths[0, 0] = 0
    for i in range(l1):
        j_start = max(0, i - max(0, l1 - l2) - window + 1)
        j_end = min(l2, i + max(0, l2 - l1) + window)
        for j in range(j_start, j_end):
            d = s1[i] - s2[j]
            cost = d ** 2
            paths[i + 1, j + 1] = cost + min(paths[i, j + 1], paths[i + 1, j], paths[i, j])

    paths = np.sqrt(paths)
    s = paths[l1, l2]
    return s, paths.T


s1 = [1, 2, 0, 1, 1, 2]
s2 = [1, 0, 1]

distance, paths = warping_paths(s1, s2)

print(distance)
print(paths)
