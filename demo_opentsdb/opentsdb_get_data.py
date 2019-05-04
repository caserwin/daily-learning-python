#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-28 14:44
# @Author  : erwin
import datetime
import time
from demo_opentsdb.opentsdb_conn import OpenTSDBClient

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
            "tags": {
                "component": "component1",
                "servertype": "stype1",
                "cluster": "XYD",
                "errortype": "etype1"
            }
        }
    ]
}

oc = OpenTSDBClient()
raw_data = oc.get_data_by_post(query_cond_dic)

print(raw_data)