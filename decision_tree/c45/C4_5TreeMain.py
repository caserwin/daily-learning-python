from decision_tree.c45.C4_5Tree import *
from decision_tree.result_explain import TreeExplain
import decision_tree.draw.treePlotter as tp

if __name__ == '__main__':
    dtree = C4_5DTree()

    # labels = ["ISREGISTER", "USERTYPE", "USERBROWSER", "JOINMETHOD", "SYSTEM"]
    # dtree.loadDataSet("/Users/cisco/workspace/mygit/daily-learning-python/decision_tree/data/test.dat", labels, ",")

    labels = ["ISREGISTER", "USERTYPE", "USEROS", "OSVERSION", "USERBROWSER", "BROWSERVERSION", "JOINMETHOD",
              "SERVICETYPE", "SERVICEID", "SITEVERSION", "COUNTRY", "PLATFORM", "SYSTEM", "ISHOST"]
    dtree.loadDataSet("/Users/cisco/workspace/mygit/daily-learning-python/decision_tree/data/dataset.dat", labels, ",")

    # labels = ["ID", "ISREGISTER", "USERTYPE", "USEROS", "OSVERSION", "USERBROWSER", "BROWSERVERSION", "JOINMETHOD",
    #           "SERVICETYPE", "SERVICEID", "SITEVERSION", "COUNTRY", "PLATFORM", "SYSTEM", "ISHOST"]
    # dtree.loadDataSet("/Users/cisco/workspace/mygit/daily-learning-python/decision_tree/data/dataset_id.dat", labels, ",")

    # 训练
    dtree.train()

    # 画图
    tp.createPlot(dtree.tree)
    # 解释
    tx = TreeExplain()
    tx.explain(dtree.tree)
    [print(info) for info in tx.getRes()]

    # vector = ['WINDOWS', 'RETURN', 'IE', 'TRUE']
    # print("真实输出", "no", "  ->  ", "决策树输出", dtree.predict(dtree.tree, labels, vector))

    # # dtree.storeTree(dtree.tree, "data.tree")
    # # mytree = dtree.grabTree("data.tree")
