# -*- coding: utf-8 -*-
# @Time    : 2018/8/3 下午12:36
# @Author  : yidxue

import core.util.file_util as fu
import re

if __name__ == '__main__':
    ls = fu.FileUtil.read_file("/Users/cisco/workspace/mygit/daily-learning-python/core/util/file/data_develop.gitbook")
    regex = re.compile(r'\d+\.md')
    res = []
    for line in ls:
        matchObj = regex.findall(line)
        res.extend([int(i.split(".")[0]) for i in matchObj])

    res.sort()
    for i, s in enumerate(res):
        print(str(i + 1) + "==>" + str(s))

    max_num = res[len(res) - 1]
    print("=" * 40)
    for i in range(1, max_num + 1):
        if i not in res:
            print("[" + str(i) + "](" + str(i) + ".md)")
