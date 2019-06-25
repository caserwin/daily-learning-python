#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-29 09:44
# @Author  : erwin
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from common.util_function import *

data = pd.read_csv('./data/voice.csv')
print_br(data.sample(5))

sns.heatmap(data.corr())
plt.show()
