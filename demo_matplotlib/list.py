# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 下午4:29
# @Author  : yidxue
import numpy as np
import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

s1 = np.array([1, 2, 0, 1, 1, 2, 0, 1, 1, 2, 0, 1, 1, 2, 0, 1])
s2 = np.array([0, 1, 1, 2, 0, 1, 1, 2, 0, 1, 1, 2, 0, 1, 1, 2])
s3 = np.array([0.8, 1.5, 0, 1.2, 0, 0, 0.6, 1, 1.2, 0, 0, 1, 0.2, 2.4, 0.5, 0.4])

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
