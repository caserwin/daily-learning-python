#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-12 12:52
# @Author  : erwin
import requests
import json


class OpenTSDBClient(object):
    config_key = 'opentsdb'

    def __init__(self):
        self.host = '10.29.42.44'
        self.port = '4242'
        # 长连接写入
        self.session = requests.Session()
        self.opentsdb_save_url = "http://{host}:{port}/api/put?details".format(host=self.host, port=self.port)

    def single_insert(self, data):
        if not isinstance(data, dict):
            return
        r = self.session.post(url=self.opentsdb_save_url, json=data)
        try:
            res = json.loads(r.text)
        except:
            res = r.text
        return res

    def bulk_insert(self, data_ls, bulk_size):
        ls = []
        for index, item in enumerate(data_ls):
            ls.append(item)
            if len(ls) == bulk_size:
                print("第{num}批处理完毕，每一批{size}个元素".format(num=int((index + 1) / bulk_size), size=bulk_size))
                self.session.post(url=self.opentsdb_save_url, json=ls)
                ls = []
        r = self.session.post(url=self.opentsdb_save_url, json=ls)
        try:
            json.loads(r.text)
            res = {
                "rows": len(data_ls),
                "bulk_size": bulk_size
            }
        except:
            res = r.text
        return res

    def get_data_by_post(self, cond_dic):
        r = requests.post("http://{host}:{port}/api/query".format(host=self.host, port=self.port), json=cond_dic)
        if len(r.json()) > 0:
            dps = r.json()[0]['dps']
            return dps
        else:
            return None

    def close(self):
        self.session.close()
