#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-19 20:20
# @Author  : erwin
import redis
import json


class RedisClient(object):
    config_key = 'redis'

    def __init__(self):
        self.host = "localhost"
        self.port = "6379"
        self.db = "0"
        self.redis_client = redis.StrictRedis(host=self.host, port=self.port, db=self.db)

    def clear_all(self):
        """
        :return: 清空所有数据
        """
        self.redis_client.flushdb()

    def delete_key(self, keystr):
        """
        :param keystr:
        :return: 删除指定类型的key
        """
        key_list = []
        for key in self.redis_client.scan_iter(match=keystr + '*', count=10000):
            key_list.append(key)

        for key in key_list:
            self.redis_client.delete(key)

    def set_cache_data(self, contents, expire=3600 * 24):
        """
        :param contents:
        :param expire:
        :return: 批量插入数据
        """
        for content in contents:
            key = content['key']
            content.pop('key')
            self.redis_client.setex(key, expire, json.dumps(content))

    def set_single_data(self, key, value):
        """
        :param key:
        :param value:
        :return: 插入单条数据
        """
        self.redis_client.set(key, value)
        self.redis_client.save()

    def get_cache_bluk_data(self, keys):
        """
        :param keys:
        :return: 查询，这里keys 是一个list
        """
        pipe = self.redis_client.pipeline()
        pipe.mget(keys)

        res_ls = []
        for (k, v) in zip(keys, pipe.execute()):
            res_ls.extend([json.loads(item) for item in v])
        return res_ls

    def get_cache_data(self, key):
        """
        :param key:
        :return: 查询，这里key是一个字符串
        """
        keys = self.redis_client.keys(key + "*")
        pipe = self.redis_client.pipeline()
        pipe.mget(keys)
        res_ls = []
        for (k, v) in zip(keys, pipe.execute()):
            res_ls.extend([json.loads(item) for item in v])
        return res_ls


if __name__ == '__main__':
    print(RedisClient().get_cache_bluk_data(
        ["error500_component1_stype1_c1_etype1_2019-03-19_100_2019-01-19 07:10:00",
         "error500_component1_stype1_c1_etype1_2019-03-19_100_2019-01-19 07:15:00",
         "error500_component1_stype1_c1_etype1_2019-03-19_100_2019-01-19 07:20:00"]
    ))

    print(RedisClient().get_cache_data("error500_component1_stype1_c1_etype1_2019-03-19_100_2019-01-19 07:1"))

    print(RedisClient().get_cache_data("aa"))
    print(RedisClient().get_cache_bluk_data("aa"))

    RedisClient().set_single_data("aa", 1)
