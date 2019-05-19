#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-25 10:24
# @Author  : erwin
from common.util_function import *
import requests

values = [[1, 2, 3], [4, 5, 6]]

ls_res = []
tsdb_data_ls = [
    {
        "metric": "sys.error502.raw",
        "timestamp": 1556267320,
        "value": 0.8,
        "tags": {
            "component": "B",
        }
    },
    {
        "metric": "sys.error502.raw",
        "timestamp": 1556267321,
        "value": 0.7,
        "tags": {
            "component": "B",
        }
    },
    {
        "metric": "sys.error502.raw",
        "timestamp": 1556267322,
        "value": 0.6,
        "tags": {
            "component": "A",
        }
    },
    {
        "metric": "sys.error502.raw",
        "timestamp": 1556267323,
        "value": 0.1,
        "tags": {
            "component": "A",
        }
    },
    {
        "metric": "sys.error502.raw",
        "timestamp": 1556267324,
        "value": 9,
        "tags": {
            "component": "A",
        }
    }
]


r = requests.post("http://10.29.42.44:4242/api/put?details", json=tsdb_data_ls)
print(r.text)
