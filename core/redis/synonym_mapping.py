# -*- coding: utf-8 -*-

import redis
import ConfigParser


class RedisServe(object):
    def __init__(self):
        # 读配置文件
        cf = ConfigParser.ConfigParser()
        cf.read("./config.conf")
        self.host = cf.get("redis_conf", "host").strip()
        self.port = int(cf.get("redis_conf", "port").strip())
        self.db = int(cf.get("redis_conf", "db"))
        self.dict_path = cf.get("dict_conf", "dict_path")
        self.r_conn = redis.StrictRedis(host=self.host, port=self.port, db=self.db)

        line_count = self.getDictLineNum(self.dict_path)
        if self.r_conn.dbsize() == 0 or self.r_conn.dbsize() != line_count:
            print('插入或更新redis同义词词典')
            self.setRedis(self.r_conn, self.dict_path)

    def setRedis(self, redis_conn, txt_path):
        # 清空所有数据
        self.clearAll()
        with open(txt_path, "r") as in_file:
            for line in in_file:
                # line格式:先简称,再全称,即把简称映射为全称。
                strs = line.split()
                redis_conn.set(strs[0], strs[1])
            redis_conn.save()

    def getConn(self):
        # 返回客户端对象
        return self.r_conn

    def clearAll(self):
        # 清空所有数据
        self.r_conn.flushdb()

    def getDictLineNum(self, txt_path):
        # 统计行数，根据dict文件中的行数和redis数据库中同义词对数量，判断是否需要更新redis。
        count = -1
        for count, line in enumerate(open(txt_path, 'rU')):
            pass
        count += 1
        return count


if __name__ == "__main__":
    redis_serve = RedisServe()
    redis_conn = redis_serve.getConn()
    redis_serve.setRedis(redis_conn, './synonym.dict')
    print(redis_conn.get('招行'))
