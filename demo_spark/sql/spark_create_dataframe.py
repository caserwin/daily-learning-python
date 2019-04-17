# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 上午10:41
# @Author  : yidxue

import pandas as pd
from pyspark.sql import SparkSession


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

    df = create_df(spark)
    df.printSchema()
    df.show(20, truncate=False)
