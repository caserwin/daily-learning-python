# -*- coding: utf-8 -*-
# @Time    : 2019/1/25 上午9:34
# @Author  : yidxue
import pandas as pd
import numpy as np
import machine_learning.similarity.time_series_util.attenuate_weight1 as cl1
import machine_learning.similarity.time_series_util.attenuate_weight2 as cl2
import matplotlib.pyplot as plt

dfStandardizedLOSS = pd.read_csv("test.csv")
s1 = np.array(dfStandardizedLOSS.iloc[:, 21])
s2 = np.array(dfStandardizedLOSS.iloc[:, 22])
s3 = np.array(dfStandardizedLOSS.iloc[:, 13])

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

# 更新前距离
distance12, paths12 = cl1.TimeSeriesSimilarity(s1, s2)
distance13, paths13 = cl1.TimeSeriesSimilarity(s1, s3)
distance23, paths23 = cl1.TimeSeriesSimilarity(s2, s3)

print("更新前s1和s2距离：" + str(distance12))
print("更新前s1和s3距离：" + str(distance13))
print("更新前s2和s3距离：" + str(distance23))

print("=" * 40)
# 策略1
best_path12 = cl1.best_path(paths12)
best_path13 = cl1.best_path(paths13)
best_path23 = cl1.best_path(paths23)

com_ls12 = cl1.get_common_seq(best_path12)
com_ls13 = cl1.get_common_seq(best_path13)
com_ls23 = cl1.get_common_seq(best_path23)

weight12 = cl1.calculate_attenuate_weight(len(best_path12), com_ls12)
weight13 = cl1.calculate_attenuate_weight(len(best_path13), com_ls13)
weight23 = cl1.calculate_attenuate_weight(len(best_path23), com_ls23)

print("策略1，更新后s1和s2距离：" + str(distance12 * weight12))
print("策略1，更新后s1和s3距离：" + str(distance13 * weight13))
print("策略1，更新后s2和s3距离：" + str(distance23 * weight23))

print("=" * 40)
# 策略2
distance12, paths12, max_sub12 = cl2.TimeSeriesSimilarityImprove(s1, s2)
distance13, paths13, max_sub13 = cl2.TimeSeriesSimilarityImprove(s1, s3)
distance23, paths23, max_sub23 = cl2.TimeSeriesSimilarityImprove(s2, s3)

weight12 = cl2.calculate_attenuate_weight(len(s1), len(s2), max_sub12)
weight13 = cl2.calculate_attenuate_weight(len(s1), len(s3), max_sub13)
weight23 = cl2.calculate_attenuate_weight(len(s2), len(s3), max_sub23)

print("策略2，更新后s1和s2距离：" + str(distance12 * weight12))
print("策略2，更新后s1和s3距离：" + str(distance13 * weight13))
print("策略2，更新后s2和s3距离：" + str(distance23 * weight23))
