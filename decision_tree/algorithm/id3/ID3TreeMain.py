from decision_tree.algorithm.id3.ID3Tree import *
from decision_tree.util.explain.result_explain import TreeExplain
import decision_tree.util.draw.treePlotter as tp
import json

if __name__ == '__main__':
    dtree = ID3DTree()

    # labels = ["ISREGISTER", "USERTYPE", "USERBROWSER", "JOINMETHOD", "SYSTEM"]
    # dtree.loadDataSet("/Users/cisco/workspace/mygit/daily-learning-python/decision_tree/data/test.dat", labels, ",")

    labels = ["ISREGISTER", "USERTYPE", "USEROS", "OSVERSION", "USERBROWSER", "BROWSERVERSION", "JOINMETHOD",
              "SERVICETYPE", "SERVICEID", "SITEVERSION", "PLATFORM", "SYSTEM", "ISHOST"]
    dtree.loadDataSet("/Users/cisco/workspace/mygit/daily-learning-python/decision_tree/data/2018-04-18-clean-12w.csv", labels, ",")

    # labels = ["ID", "ISREGISTER", "USERTYPE", "USEROS", "OSVERSION", "USERBROWSER", "BROWSERVERSION", "JOINMETHOD",
    #           "SERVICETYPE", "SERVICEID", "SITEVERSION", "COUNTRY", "PLATFORM", "SYSTEM", "ISHOST"]
    # dtree.loadDataSet("/Users/cisco/workspace/mygit/daily-learning-python/decision_tree/data/dataset_id.dat", labels, ",")

    # 训练
    dtree.train()

    # 保存模型
    dtree.storeTree(dtree.tree, "ID3_2018-04-18.model")

    # 画图
    # tp.createPlot(dtree.tree)

    # 读取模型
    model = dtree.grabTree("ID3_2018-04-18.model")
    print(json.dumps(model, ensure_ascii=False))
    # 解释
    tx = TreeExplain()
    tx.explain(model)
    [print(info) for info in tx.getRes()]

    # 预测
    # vector = ['WINDOWS', 'RETURN', 'IE', 'TRUE']
    # print("真实输出", "no", "  ->  ", "决策树输出", dtree.predict(dtree.tree, labels, vector))
