# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 上午10:09
# @Author  : yidxue
import numpy as np
from machine_learning.similarity.time_series_similar import TimeSeriesSimilarity
import matplotlib.pyplot as plt


def myprint(paths):
    for path in paths:
        print(path)


if __name__ == '__main__':
    # s1 = np.array([2, 0, 100, 1, 2, 0, 1, 2, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1])
    # # s1 = np.array([2, 0, 1, 1, 2, 0, 10, 2, 0, 1, 1])
    # s2 = np.array([2, 0, 1, 1, 2, 0, 1, 200, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1])
    s3 = np.array([1.5, 5, 1.2, 0, 6, 2, 1, 8, 0, 1])

    s1 = np.array([0, 0, 0, 1, 0, 1, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    # s1 = np.array([2, 0, 1, 1, 2, 0, 10, 2, 0, 1, 1])
    s2 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    d, paths = TimeSeriesSimilarity(s1, s2)
    print(d)
    myprint(paths)
    print("=" * 40)
    d, paths = TimeSeriesSimilarity(s1, s3)
    print(d)
    myprint(paths)
    # print(paths)

    plt.figure()
    plt.subplot(311)
    plt.ylabel("s1")
    plt.plot(s1)
    plt.subplot(312)
    plt.ylabel("s2")
    plt.plot(s2)
    plt.subplot(313)
    plt.ylabel("s3")
    plt.plot(s3)

    plt.show()

    # best_path12 = dtw.best_path(paths12)
    # dtwvis.plot_warpingpaths(s1, s2, paths12, best_path12)
    # print(best_path12)
    #
    # best_path13 = dtw.best_path(paths13)
    # dtwvis.plot_warpingpaths(s1, s3, paths13, best_path13)
    # print(best_path13)
