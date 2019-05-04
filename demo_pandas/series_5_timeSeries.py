#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-15 21:12
# @Author  : erwin
import pandas as pd
import numpy as np
import json
from common.util_function import *

rng = pd.date_range('1/1/2012', periods=100, freq='S')
ts = pd.Series(np.random.randint(0, 10, len(rng)), index=rng)

print_line("原始数据")
print_br(ts)

print_line("聚合数据")
print_br(ts.resample('1Min').sum())
print_br(ts.resample('1Min').mean())


print_line("时间序列示例")
with open('./data/time_series_json_data') as f:
    body = json.load(f)

df = pd.DataFrame(data=body.get("context", []))
temp_series = pd.Series(data=np.array(df["fail"]),
                        index=df["date"].map(lambda x: pd.to_datetime(x).replace(second=0)))

print_br(len(temp_series))
print_br(len(temp_series[~temp_series.index.duplicated()]))

oper_series = temp_series[~temp_series.index.duplicated()].resample('5min').ffill()
print_br(oper_series)
