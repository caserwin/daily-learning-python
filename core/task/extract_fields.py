#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-13 16:05
# @Author  : erwin
from common.file_util import FileUtil
import json


def iter_extract_field(item, fields_ls=None, prefix=''):
    if fields_ls is None:
        fields_ls = []
    if not isinstance(item[1], dict):
        fields_ls.append(prefix)
    else:
        for k, v in item[1].items():
            p = k if prefix == '' else prefix + "." + k
            iter_extract_field((k, v), fields_ls, p)


if __name__ == '__main__':
    # 读文件，并转成json list
    text_ls = FileUtil.read_file('./task/details.json')
    json_ls = [json.loads(item) for item in text_ls]

    # 加到set中
    fields_set = set({})
    for json in json_ls:
        fields_ls = []
        iter_extract_field(('', json), fields_ls)
        fields_set.update(fields_ls)

    # 字典序排序
    fields_dic_sort = sorted(fields_set)

    # 输出到文件
    print(len(fields_dic_sort))
    FileUtil.write_ls_file("./task/fields_dict.txt", fields_dic_sort)
