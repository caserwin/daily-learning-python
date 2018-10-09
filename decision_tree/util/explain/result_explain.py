# encoding:utf-8

from decision_tree.util.explain.dic import test_dic
import collections


class TreeExplain(object):

    def __init__(self):
        self.res = []
        self.info_stack = collections.OrderedDict()

    def explain(self, dic, string='', num=0):
        self.info_stack[num] = string
        for feature in list(dic.keys()):
            if isinstance(dic[feature], dict):
                info = self.info_stack[num]
                if num % 2 == 0:
                    info += feature + "="
                else:
                    info += feature + ","
                self.explain(dic[feature], info, num + 1)
            else:
                self.res.append(string + feature + "，类别为：" + dic[feature])

    def getRes(self):
        return self.res


if __name__ == '__main__':
    tx = TreeExplain()
    tx.explain(test_dic)
    res_ls = tx.getRes()
    for info in res_ls:
        print(info)
