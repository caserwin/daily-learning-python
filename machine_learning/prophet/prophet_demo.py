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

operDF = pd.read_json('./test.json')
operDF.columns = ["time", "rate"]
operDF = operDF.sort_values("time").copy()

# ts_daily = pd.date_range((dt.today() + DateOffset(days=-15)).strftime("%Y-%m-%d"), periods=3580, freq='5T')
tempS = pd.Series(data=np.array(operDF["rate"]), index=operDF["time"].map(lambda x: pd.to_datetime(x)
                                                                                 .replace(second=0)))
df = tempS.resample('5min').asfreq().iloc[0:3580]
df.sort_index()

finalDF = pd.DataFrame(df.sort_index().values, index=df.sort_index().index).dropna().reset_index()
finalDF.columns = ['ds', 'y']

m = Prophet(changepoint_prior_scale=0.001)
m.fit(finalDF)

future = m.make_future_dataframe(periods=120, freq='H')
fcst = m.predict(future)
print(fcst)
