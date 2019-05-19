#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-17 17:39
# @Author  : erwin
import time
import math
import requests


def get_value(num):
    return math.sin(num) + 1


def send_json(json, s):
    r = s.post("http://10.29.42.44:4242/api/put?details", json=json)
    return r.text


def main():
    s = requests.Session()
    a = int(time.time()) - 100000
    ls = []
    for i in range(1, 100000):
        json = {
            "metric": "sys.batch.test6",
            "timestamp": a,
            "value": get_value(i),
            "tags": {
                "host": "web01",
                "dc": "lga"
            }
        }
        i += 0.01
        a += 1
        ls.append(json)
        if len(ls) == 50:
            send_json(ls, s)
            ls = []
    send_json(ls, s)


if __name__ == "__main__":
    start = time.time()
    main()
    print(time.time() - start)
