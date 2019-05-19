#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-17 17:16
# @Author  : erwin
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
from component.demo_opentsdb.opentsdb_conn import OpenTSDBClient
import pandas as pd

remote_zip = urlopen('https://archive.ics.uci.edu/ml/machine-learning-databases/00357/occupancy_data.zip')
df = pd.read_csv(BytesIO(ZipFile(BytesIO(remote_zip.read())).read('datatraining.txt')))

tsdf = df.iloc[:, 1:].set_index(df["date"].copy().map(lambda x: pd.to_datetime(x))).resample(
    '1min').ffill().reset_index()
tsdf.date = tsdf.date.map(lambda x: int(x.timestamp()))

# opentsdb 写入
oc1 = OpenTSDBClient()
tsdb_temperature_temperature = [
    {
        "metric": "wbx.weather.temperature",
        "timestamp": value[0],
        "value": value[1],
        "tags": {
            "feature": 'temperature'
        }
    } for value in tsdf.values
]

tsdb_temperature_occupancy = [
    {
        "metric": "wbx.weather.temperature",
        "timestamp": value[0],
        "value": value[6],
        "tags": {
            "feature": 'occupancy'
        }
    } for value in tsdf.values
]

oc1.bulk_insert(tsdb_temperature_temperature, 100)
oc1.bulk_insert(tsdb_temperature_occupancy, 100)
