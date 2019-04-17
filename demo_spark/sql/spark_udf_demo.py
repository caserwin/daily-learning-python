# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 上午10:34
# @Author  : yidxue

from pyspark.sql.functions import udf
from pyspark.sql.types import BooleanType
from pyspark.sql import SparkSession
from demo_spark.sql.spark_create_dataframe import create_df
import re

filter_text_udf = udf(lambda z: filter_text(z), BooleanType())


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
