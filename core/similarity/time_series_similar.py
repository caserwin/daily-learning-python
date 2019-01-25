# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 上午10:39
# @Author  : yidxue
import numpy as np
from dtaidistance import dtw
from dtaidistance import dtw_visualisation as dtwvis
from core.similarity.time_series_util.attenuate_weight1 import *

float_formatter = lambda x: "%.2f" % x
np.set_printoptions(formatter={'float_kind': float_formatter})


def TimeSeriesSimilarity(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    paths = np.full((l1 + 1, l2 + 1), np.inf)  # 全部赋予无穷大
    paths[0, 0] = 0
    for i in range(l1):
        for j in range(l2):
            d = s1[i] - s2[j]
            cost = d ** 2
            paths[i + 1, j + 1] = cost + min(paths[i, j + 1], paths[i + 1, j], paths[i, j])

    paths = np.sqrt(paths)
    s = paths[l1, l2]
    return s, paths.T


def best_path(paths):
    """Compute the optimal path from the nxm warping paths matrix."""
    i, j = int(paths.shape[0] - 1), int(paths.shape[1] - 1)
    p = []
    if paths[i, j] != -1:
        p.append((i - 1, j - 1))
    while i > 0 and j > 0:
        c = np.argmin([paths[i - 1, j - 1], paths[i - 1, j], paths[i, j - 1]])
        if c == 0:
            i, j = i - 1, j - 1
        elif c == 1:
            i = i - 1
        elif c == 2:
            j = j - 1
        if paths[i, j] != -1:
            p.append((i - 1, j - 1))
    p.pop()
    p.reverse()
    return p


if __name__ == '__main__':
    # ====================== 问题描述 ===========================
    s1 = np.array([1, 2, 0, 1, 1, 2, 0, 1, 1, 2, 0, 1, 1, 2, 0, 1])
    s2 = np.array([0, 1, 1, 2, 0, 1, 1.7, 2, 0, 1, 1, 2, 0, 1, 1, 2])
    s3 = np.array([0.8, 1.5, 0, 1.2, 0, 0, 0.6, 1, 1.2, 0, 0, 1, 0.2, 2.4, 0.5, 0.4])

    distance12, paths12 = TimeSeriesSimilarity(s1, s2)
    distance13, paths13 = TimeSeriesSimilarity(s1, s3)

    print(distance12)
    print(distance13)

    best_path12 = best_path(paths12)
    best_path13 = best_path(paths13)

    # ====================== 画图展示 ===========================
    dtwvis.plot_warpingpaths(s1, s2, paths12, best_path12)
    print(best_path12)

    dtwvis.plot_warpingpaths(s1, s3, paths13, best_path13)
    print(best_path13)
    # ====================== 改进策略 1 ===========================

    com_ls12 = get_common_seq(best_path12)
    com_ls13 = get_common_seq(best_path13)

    print(com_ls12)
    print(com_ls13)
    attenuate_weight12 = calculate_attenuate_weight(best_path12[len(best_path12) - 1][0],
                                                    best_path12[len(best_path12) - 1][1],
                                                    com_ls12)
    attenuate_weight13 = calculate_attenuate_weight(best_path13[len(best_path13) - 1][0],
                                                    best_path13[len(best_path13) - 1][1],
                                                    com_ls13)
    print("改进后:" + str(distance12 * attenuate_weight12))
    print("改进后:" + str(distance13 * attenuate_weight13))

    # ====================== 改进策略 2 ===========================


