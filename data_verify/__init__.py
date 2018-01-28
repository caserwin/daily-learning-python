# coding: utf-8

import os
import psutil
import time


def get_cpu_usage(py, time):
    print py.memory_info()
    print py.name()
    memoryUse = py.memory_info()[0] / 2. ** 30  # memory use in GB...I think
    print time, ":", memoryUse


def get_mem_usage(py, time):
    print py.memory_info()
    memoryUse = py.memory_info()[0] / 2. ** 30  # memory use in GB...I think
    print time, ":", memoryUse


if __name__ == '__main__':
    # cpu使用率
    # pid = os.getpid()
    # py = psutil.Process(pid)
    # while True:
    # get_cpu_usage(py, int(time.time()))
        # time.sleep(10)

    # 内存使用率
    # values = psutil.virtual_memory()
    # total = values.total
    # available = values.available
    # print float(available)/total

    import psutil

    for x in range(3):
        print psutil.cpu_percent(interval=1)

    print(psutil.virtual_memory())
