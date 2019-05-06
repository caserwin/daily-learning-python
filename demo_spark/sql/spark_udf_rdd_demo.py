# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 上午10:34
# @Author  : yidxue
from pyspark.sql.functions import udf
from pyspark.sql.types import BooleanType
from pyspark.sql import SparkSession
import re
import pandas as pd

filter_text_udf = udf(lambda z: filter_text(z), BooleanType())


def create_df(spark):
    df_pd = pd.DataFrame(
        data={'col1': [1, 2, 3],
              'col2': [-1.0, 0.5, 2.7],
              'col3': [[1, 2], [3, 4, 5], [6, 7, 8, 9]],
              'col4': ["text1", "text2 aa", "text3 cc"]}
    )
    return spark.createDataFrame(df_pd)


def filter_text(text):
    if len(re.split("\\s+", text)) < 2:
        return False
    else:
        return True


if __name__ == '__main__':
    spark = SparkSession \
        .builder \
        .appName("test") \
        .config("spark.master", "local[*]") \
        .getOrCreate()

    df = create_df(spark)
    df.show(20, truncate=False)
    df.filter(filter_text_udf("col4")).show(20, truncate=False)
    spark.stop()
