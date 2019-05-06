#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-05 16:38
# @Author  : erwin
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType
from pyspark.sql.functions import udf
import pandas as pd

slen = udf(lambda s: len(s), IntegerType())


def create_df(spark):
    df_pd = pd.DataFrame(
        data={'col1': [1, 2, 3],
              'col2': [-1.0, 0.5, 2.7],
              'col3': [[1, 2], [3, 4, 5], [6, 7, 8, 9]],
              'col4': ["text1", "text2 aa", "text3 cc"]}
    )
    return spark.createDataFrame(df_pd)


if __name__ == '__main__':
    spark = SparkSession \
        .builder \
        .appName("test") \
        .config("spark.master", "local[*]") \
        .getOrCreate()

    spark.udf.register("slen", slen)

    df = create_df(spark)
    df.select(
        "col1",
        "col2",
        "col3",
        slen("col4")
    ).show()
