#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-09 14:34
# @Author  : erwin
from multiprocessing import Pool
from component.demo_opentsdb.opentsdb_conn import OpenTSDBClient
import time


def task(name):
    print('process %s is running' % name)
    # 插入opentsdb
    oc = OpenTSDBClient()
    tsdb_data = {
        "metric": "sys.error501",
        "timestamp": 1556076325,
        "value": 12.3,
        "tags": {
            "component": 12.3
        }
    }

    oc.single_insert(tsdb_data)
    # time.sleep(3)
    print('process %s done' % name)


if __name__ == '__main__':
    start_time = time.time()
    # 创建进程池，指定最大并发进程数
    pool = Pool(processes=4)
    for i in range(4):
        # 每个进程调用task函数， 用元组的形式传递参数
        pool.apply_async(task, (i,))
    # 关闭进程池
    pool.close()
    # 主进程等待进程池中的进程执行完毕
    pool.join()
    end_time = time.time()
    duration = end_time - start_time
    print('main process duration: %.3fs' % duration)
