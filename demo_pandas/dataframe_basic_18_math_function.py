#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-18 18:12
# @Author  : erwin
import numpy as np
import pandas as pd
from common.util_function import *

data = np.array([[1, 2, 3, 4],
                 [4, 5, 6, 8],
                 [2, 3, 5, 9]])
df = pd.DataFrame(data=data, index=['a', 'b', 'c'], columns=['A', 'B', 'C', 'D'])


