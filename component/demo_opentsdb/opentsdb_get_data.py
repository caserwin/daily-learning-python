#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-28 14:44
# @Author  : erwin
import datetime
import time
from component.demo_opentsdb.opentsdb_conn import OpenTSDBClient
import pandas as pd

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

train_day = 10
now_date = datetime.datetime.now().strftime("%Y-%m-%d") + " 00:00:00"
pass_date = (datetime.datetime.now() + datetime.timedelta(days=-train_day)).strftime("%Y-%m-%d") + " 00:00:00"

now_timestamp = int(time.mktime(time.strptime(now_date, '%Y-%m-%d %H:%M:%S')))
pass_timestamp = int(time.mktime(time.strptime(pass_date, '%Y-%m-%d %H:%M:%S')))

query_cond_dic = {
    "start": pass_timestamp,
    "end": now_timestamp,
    "queries": [
        {
            "aggregator": "none",
            "metric": "sys.error500.raw",
            # "downsample": "30m-avg",
            "tags": {
                "cluster": "L",
            }
        }
    ]
}

oc = OpenTSDBClient()
raw_datas = oc.get_data_by_post_all(query_cond_dic)

# OpenTSDB 数据转成 Pandas DataFrame
records = {data.get("tags").get("cluster") + "_" + data.get("tags").get("errortype"): data.get("dps") for data in
           raw_datas}

df = pd.DataFrame(data=records)
print(df.head(100))

df.to_csv("./opentsdb_L.csv", sep=",", index=True, header=True)
