#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-16 16:44
# @Author  : erwin
import pandas as pd
from demo_pandas.function.util_function import *

print_line("方式1：value_list是数值，key_list是索引")
print_br(pd.Series(range(4), index=["a", "b", "c", "d"]))

print_line("方式2：因为没有给Series指定索引，所以此时会使用默认索引(从0到N-1)。")
print_br(pd.Series([1, 2, 3, 4]))

print_line("方式3：通过字典来创建Series对象")
print_br(pd.Series({'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}))

tmp = pd.Series({item[0]: item[1] for item in [('2018-12-28 00:00:00', 159.80092592592592), ('2018-12-28 00:01:00', 85.24064171122994)]})
print(tmp)
