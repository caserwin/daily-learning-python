# -*- coding: utf-8 -*-
# @Time    : 2019/1/25 上午9:34
# @Author  : yidxue
import pandas as pd
from core.similarity.time_series_util.attenuate_weight2 import *
from core.similarity.time_series_util.attenuate_weight1 import *
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

# 策略1
distance12, paths12 = TimeSeriesSimilarity(s1, s2)
distance13, paths13 = TimeSeriesSimilarity(s1, s3)
distance23, paths23 = TimeSeriesSimilarity(s2, s3)

print("更新前s1和s2距离：" + str(distance12))
print("更新前s1和s3距离：" + str(distance13))
print("更新前s2和s3距离：" + str(distance23))

best_path12 = best_path(paths12)
best_path13 = best_path(paths13)
best_path23 = best_path(paths23)

com_ls12 = get_common_seq(best_path12)
com_ls13 = get_common_seq(best_path13)
com_ls23 = get_common_seq(best_path23)

weight12 = calculate_attenuate_weight(best_path12[len(best_path12) - 1][0], best_path12[len(best_path12) - 1][1],
                                      com_ls12)
weight13 = calculate_attenuate_weight(best_path13[len(best_path13) - 1][0], best_path13[len(best_path13) - 1][1],
                                      com_ls13)
weight23 = calculate_attenuate_weight(best_path23[len(best_path23) - 1][0], best_path23[len(best_path23) - 1][1],
                                      com_ls23)

print("策略1，更新后s1和s2距离：" + str(distance12 * weight12))
print("策略1，更新后s1和s3距离：" + str(distance13 * weight13))
print("策略1，更新后s2和s3距离：" + str(distance23 * weight23))

print("=" * 40)
# 策略2
distance12, paths12, max_sub12 = TimeSeriesSimilarityImprove(s1, s2)
distance13, paths13, max_sub13 = TimeSeriesSimilarityImprove(s1, s3)
distance23, paths23, max_sub23 = TimeSeriesSimilarityImprove(s2, s3)

print("策略2，更新前s1和s2距离：" + str(distance12))
print("策略2，更新前s1和s3距离：" + str(distance13))
print("策略2，更新前s2和s3距离：" + str(distance23))

weight12 = calculate_attenuate_weight(len(s1), len(s2), max_sub12)
weight13 = calculate_attenuate_weight(len(s1), len(s3), max_sub13)
weight23 = calculate_attenuate_weight(len(s2), len(s3), max_sub23)

print("策略2，更新后s1和s2距离：" + str(distance12 * weight12))
print("策略2，更新后s1和s3距离：" + str(distance13 * weight13))
print("策略2，更新后s2和s3距离：" + str(distance23 * weight23))
