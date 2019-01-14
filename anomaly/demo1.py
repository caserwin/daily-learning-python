# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 下午8:20
# @Author  : yidxue
from __future__ import division
import numpy
import datetime
import pandas as pd


def get_all_file_path(path):
    """
    循环遍历,得到一个文件夹第一层下的文件路径
    """
    import os
    file_name_list = os.listdir(path)
    return [path + os.sep + file_name for file_name in file_name_list]


def read_file(path_ls):
    """
    读数据
    """
    map = {}
    for file_path in path_ls:
        with open(file_path, mode="r") as in_file:
            for i, line in enumerate(in_file):
                if not (line.strip == "" or line.startswith('clusterid')):
                    data = line.strip().split(",")
                    cluster = data[0]
                    timestamp = data[1]
                    rtts = float(data[7])
                    if cluster in map.keys():
                        map[cluster][timestamp] = rtts
                    else:
                        cluster_map = {timestamp: rtts}
                        map[cluster] = cluster_map
    return map


def write_file(file_path, context_ls, method='a'):
    """
    写数据到一个文件
    :param file_path:
    :param method: 'a'表示默认为追加方式, 'wb'表示覆盖或者创建文件写入
    :param context:
    """
    with open(file_path, method) as fo:
        for text in context_ls:
            fo.write(text + "\n")
    # 关闭打开的文件
    fo.close()


def calculate_std(dps, moving_average):
    variance = 0
    flag_list = moving_average.isnull()
    count = 0
    for index in range(len(dps)):
        if flag_list[index]:
            count += 1
            continue
        variance += (dps[index] - moving_average[index]) ** 2
    variance /= (len(dps) - count)
    return numpy.sqrt(variance)


day = '2018-12-24'

# 1. 读数据
path = '/Users/cisco/Downloads/abnormal_value_2018lastweek/abnormal_value_{day}.csv'
path_ls = get_all_file_path(path.format(day=day))

# 2. 读数据
data_dict = read_file(path_ls)

# 3. 每个cluster时间戳进行排序
DESC = False
## 列表推导生成字典，这个字典的value的是排序后的另一个字典
data_sort = {
    cluster: sorted(data_dict[cluster].items(), key=lambda d: datetime.datetime.strptime(d[0], '%Y-%m-%d %H:%M:%S'),
                    reverse=DESC)
    for cluster in data_dict.keys()}

cluster = {}
for key in data_sort.keys():
    cluster[key] = pd.Series({item[0]: item[1] for item in data_sort[key]})

# 4. 异常检测
for key in cluster.keys():
    dps = pd.Series(cluster[key])
    ewma_line = dps.ewm(span=4).mean()
    ewma_std = calculate_std(dps, ewma_line)
    result = []
    for index in ewma_line.index:
        if not (ewma_line[index] - ewma_std <= dps[index] <= ewma_line[index] + ewma_std):
            result.append(key + "," + index + "," + str(dps[index]) + ",1")
        else:
            result.append(key + "," + index + "," + str(dps[index]) + ",0")
    # 存数据
    write_file('/Users/cisco/Desktop/{day}.csv'.format(day=day), result)
