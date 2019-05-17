# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 上午7:21
# @Author  : yidxue
import logging
import numpy as np
import pandas as pd
from fbprophet import Prophet

logging.getLogger('fbprophet').setLevel(logging.ERROR)
import warnings

warnings.filterwarnings("ignore")
from pandas.tseries.offsets import *
from datetime import datetime as dt

operDF = pd.read_json('./test_fbprophet.json')
operDF.columns = ["timeMins", "500rate"]
operDF = operDF.sort_values("timeMins").copy()

# ts_daily = pd.date_range((dt.today() + DateOffset(days=-15)).strftime("%Y-%m-%d"), periods=3580, freq='5T')
tempS = pd.Series(data=np.array(operDF["500rate"]), index=operDF["timeMins"].map(lambda x: pd.to_datetime(x).replace(second=0)))
df = tempS.resample('5min').asfreq().iloc[0:3580]
df.sort_index()

finalDF = pd.DataFrame(df.sort_index().values, index=df.sort_index().index).dropna().reset_index()
finalDF.columns = ['ds', 'y']

m = Prophet(changepoint_prior_scale=0.001)
m.fit(finalDF)

future = m.make_future_dataframe(periods=120, freq='H')
fcst = m.predict(future)
print(fcst)

##
# ##检测
# def getGapBetweenThrshActural(n):
#     return pd.merge(finalDF.tail(n), fcst, on='ds')["y"] - pd.merge(finalDF.tail(n), fcst, on='ds')["yhat_upper"]
#
#
# def isOut(x):
#     if x > 0:
#         return 1
#     else:
#         return 0
#
#
# # 连续8个点在范围外
# out8 = getGapBetweenThrshActural(8)
# # 三个小时里面有14个点在范围外
# out18 = getGapBetweenThrshActural(18)
#
# if out8.map(lambda x: x > 0).all() or out18.map(lambda x: isOut(x)).sum() >= 14:
#     fig_anormaly = m.plot(fcst)
#     fig_anormaly.savefig('data/anormalyImg')
#     pd.merge(finalDF, fcst, on='ds').to_csv('data/anormalyData')
#     fig_seasoning = m.plot_components(fcst)
#     print("翻了")
#
# # 副作用
# fig_anormaly = m.plot(fcst)
