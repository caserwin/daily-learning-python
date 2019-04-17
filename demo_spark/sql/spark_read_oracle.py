# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 上午11:14
# @Author  : yidxue
from pyspark.storagelevel import *
from pyspark.sql import SparkSession
import datetime
import time


def getPredicates(day, after_day):
    ls = [
        (day + " 00:00:00", day + " 06:00:00"),
        (day + " 06:00:00", day + " 09:00:00"),
        (day + " 09:00:00", day + " 12:00:00"),
        (day + " 12:00:00", day + " 14:00:00"),
        (day + " 14:00:00", day + " 16:00:00"),
        (day + " 16:00:00", day + " 18:00:00"),
        (day + " 18:00:00", day + " 21:00:00"),
        (day + " 21:00:00", after_day + " 00:00:00")
    ]

    return map(lambda x: ("endtime >= TO_DATE('{0}','YYYY-MM-DD HH24:MI:SS')"
                          + " and endtime <= TO_DATE('{1}','YYYY-MM-DD HH24:MI:SS')").format(x[0], x[1]), ls)


def getDF(spark, day):
    after_day = (datetime.datetime.strptime(day, "%Y-%m-%d") + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    jdbc_url = "jdbc:oracle:thin:@//127.0.0.1:1234/sss.sss.com"
    conf = {"user": "user", "password": "pass", "driver": "oracle.jdbc.driver.OracleDriver"}
    sql = ("(SELECT siteid,confid,confname,endtime from test WHERE "
           "endtime >= TO_DATE('{0} 00:00:00', 'yyyy-MM-dd HH24:MI:SS') " +
           "AND endtime < TO_DATE('{1} 00:00:00', 'yyyy-MM-dd HH24:MI:SS'))tmp").format(
        day, after_day)
    print(sql)
    return spark.read.jdbc(jdbc_url, sql, predicates=getPredicates(day, after_day), properties=conf)


if __name__ == '__main__':
    start = time.time()
    path = "/Users/yidxue/.m2/repository/com/oracle/jdbc/ojdbc7/12.1.0.2.0/ojdbc7-12.1.0.2.0.jar"
    spark = SparkSession \
        .builder \
        .appName("test") \
        .config("spark.executor.extraClassPath", path) \
        .config("spark.driver.extraClassPath", path) \
        .config("spark.master", "local[*]") \
        .getOrCreate()

    df = getDF(spark, "2018-10-02")
    df.persist(StorageLevel(True, False, False, False))
    df.show()
    print(time.time() - start)
