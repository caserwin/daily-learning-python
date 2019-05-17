#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-05 15:47
# @Author  : erwin
import json
import time
import numpy as np
import pandas as pd
from fbprophet import Prophet
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf

weight = 0.001


def create_df(spark):
    with open('../data/json.txt') as f:
        body = json.load(f)

    df_pd = pd.DataFrame(
        data=[{
            "cluster": item.get("tags").get("cluster"),
            "errortype": item.get("tags").get("errortype"),
            "component": item.get("tags").get("component"),
            "servertype": item.get("tags").get("servertype"),
            "dps": item.get("dps")
        } for item in body]
    )
    return spark.createDataFrame(df_pd)


def cal_fbprophet(data):
    operDF = pd.DataFrame.from_records(
        [{'timestamp': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(item[0]))), 'value': item[1]}
         for item in data.items()])

    operDF.columns = ["timeMins", "500rate"]
    operDF = operDF.sort_values("timeMins").copy()
    tempS = pd.Series(data=np.array(operDF["500rate"]),
                      index=operDF["timeMins"].map(lambda x: pd.to_datetime(x).replace(second=0)))

    df = tempS.resample('5min').bfill()
    df.sort_index()

    finalDF = pd.DataFrame(df.sort_index().values, index=df.sort_index().index).dropna().reset_index()
    finalDF.columns = ['ds', 'y']

    m = Prophet(changepoint_prior_scale=weight,
                yearly_seasonality=False,
                weekly_seasonality=True,
                daily_seasonality=True
                )
    m.fit(finalDF)

    future = m.make_future_dataframe(periods=288, freq='5min')
    fcst = m.predict(future)
    return str(fcst[["ds", "yhat_upper", "yhat_lower"]].values.tolist())


if __name__ == '__main__':
    spark = SparkSession \
        .builder \
        .appName("testqqq") \
        .config("spark.master", "local[*]") \
        .getOrCreate()

    cal_fbprophet_udf = udf(lambda z: cal_fbprophet(z))
    df = create_df(spark)
    df.select("cluster",
              "errortype",
              "component",
              "servertype",
              cal_fbprophet_udf("dps")
              ) \
        .show(20, truncate=False)

