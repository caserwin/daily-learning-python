# -*- coding: utf-8 -*-

import redis
import time
import json
import ConfigParser


class RedisServe(object):
    def __init__(self):
        cf = ConfigParser.ConfigParser()
        conf_key = 'redis'
        self.host = cf.get(conf_key, "host")
        self.port = cf.get(conf_key, "port")
        self.db = cf.get(conf_key, "db")
        self.ex = cf.get(conf_key, "ex_time")
        self.r_conn = redis.StrictRedis(host=self.host, port=self.port, db=self.db)

    def set_redis(self, key, value):
        """
        add data to redis
        """
        self.r_conn.set(key, value, ex=self.ex)
        self.r_conn.save()

    def get_conn(self):
        """
        return redis connection object
        """
        return self.r_conn

    def clear_all(self):
        """
        clear all redis data
        """
        self.r_conn.flushdb()

    def get_by_key(self, key):
        """
        get data by key
        """
        return self.r_conn.get(key)

    @staticmethod
    def is_valid_date(string):
        try:
            time.mktime(time.strptime(string, "%Y-%m-%d %H:%M"))
            return True
        except:
            return False


value = {
    "search_id": "HashValueOfSth.",
    "status": 0,
    "error_message": "",
    "search_stats": {
        "number_of_bucket": 5,
        "buckets": [
            {
                "start_timestamp": "1479312000",
                "length": 86400,
                "count": 763
            },
            {
                "start_timestamp": "1479398400",
                "length": 86400,
                "count": 517
            },
            {
                "start_timestamp": "1479484800",
                "length": 86400,
                "count": 6786
            },
            {
                "start_timestamp": "1479571200",
                "length": 86400,
                "count": 3
            },
            {
                "start_timestamp": "1479657600",
                "length": 86400,
                "count": 763
            }
        ],
        "time_range": {
            "start_timestamp": "1479312000",
            "end_timestamp": "1479744000"
        },
        "counts": 109964,
    },
    "field_stats": [
        {
            "name": "channel_id",
            "distinct_count": 2,
            "values": [
                "108303156",
                "109325799"
            ],
            "value_frequency": [
                114142,
                3240
            ],
            "others_frequency": 0,
            "null_frequency": 0,

        },
        {
            "name": "_format",
            "distinct_count": 0,
            "values": [

            ],
            "value_frequency": [

            ],
            "others_frequency": 0,
            "null_frequency": 0,

        }
    ],
    "logs": {
        "begin_offset": 0,
        "count": 3,
        "keys": [
            "_timestamp",
            "latency",
            "uri",
            "_raw"
        ],
        "logs": [
            {
                "_timestamp": "1480057802018",
                "_raw": "this is my log"
            },
            {
                "_timestamp": "1480057802019",
                "_raw": "this is my log 2",
                "latency": "59ms"
            },
            {
                "_timestamp": "1480057802019",
                "_raw": "this is my log 3",
                "uri": "hz.com"
            }
        ]
    }
}

if __name__ == "__main__":
    redis_serve = RedisServe()
    begin_timestamp = "2017-01-11 17:10"
    end_timestamp = "2017-01-11 17:10"
    key = "search_id+','+host+','+log_group_ids+','+begin_timestamp+','+end_timestamp+','+begin_offset+','+log_count"

    if redis_serve.is_valid_date(begin_timestamp) and redis_serve.is_valid_date(end_timestamp):
        redis_serve.set_redis(key, json.dumps(value))
        store_value = redis_serve.get_by_key(key)
        print(json.loads(store_value))

    """
    time.sleep(30) # 休眠30秒,用于测试
    store_value = redis_serve.get_by_key(key)
    print json.loads(store_value)
    """
