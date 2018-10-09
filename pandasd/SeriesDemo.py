# -*- coding: utf-8 -*-
# @Time    : 2018/10/3 下午2:14
# @Author  : yidxue
import pandas as pd

data_dict_series = {
    '1490707920': 10,
    '1490708040': 20,
    '1490708200': None,
    '1490708100': 20,
}
pds = pd.Series(data_dict_series)

print(pds.var())
print('----------------')
print(pds.mean())
print('----------------')
print(pds.values)
print('----------------')
print(pds.index)
print('----------------')
print(pds.keys())
print('----------------')
print(pds.dropna())
print('----------------')
print(pds[[0, 1, 2]])
print('----------------')
print(pds['1490707920'])
print('----------------')
print(pds[0])

ser1 = pd.Series(range(4))
ser2 = pd.Series(range(3))

# 两个序列基于行拼接
df = pd.concat([ser1, ser2])
print(df)

# 两个序列基于列拼接
df = pd.concat([ser1, ser2], axis=1)
print(df)
