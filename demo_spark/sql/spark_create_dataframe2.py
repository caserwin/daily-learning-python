#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-05 15:47
# @Author  : erwin
import json
import pandas as pd
from pyspark.sql import SparkSession


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


if __name__ == '__main__':
    spark = SparkSession \
        .builder \
        .appName("test") \
        .config("spark.master", "local[*]") \
        .getOrCreate()

    df = create_df(spark)

    df.select("cluster",
              "errortype",
              "component",
              "servertype",
              "dps"
              ).show(20, truncate=False)
