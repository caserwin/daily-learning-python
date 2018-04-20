class TreeExplain(object):

    def __init__(self):
        self.res = []

    def explain(self, dic, string='', num=0):
        for feature in list(dic.keys()):
            if isinstance(dic[feature], dict):
                if num % 2 == 0:
                    string += feature + "="
                else:
                    string += feature + ","
                self.explain(dic[feature], string, num + 1)
            else:
                self.res.append(string + feature + "，类别为：" + dic[feature])

    def getRes(self):
        return self.res


if __name__ == '__main__':
    dic = {"JOINMETHOD": {"ActiveX": "1", "Extension": {"USERTYPE": {"NEW": "1", "RETURN": "0"}}}}
    tx = TreeExplain()
    tx.explain(dic)
    res_ls = tx.getRes()
    for info in res_ls:
        print(info)
