# encoding:utf-8
from decision_tree.algorithm.c45.C4_5Tree import *
from decision_tree.util.explain.result_explain import TreeExplain
import decision_tree.util.draw.treePlotter as tp
import json

if __name__ == '__main__':
    dtree = C4_5DTree()

    labels = ["ISREGISTER", "USERTYPE", "USERBROWSER", "JOINMETHOD", "SYSTEM"]
    dtree.loadDataSet("/Users/yidxue/workspace/mygit/daily-learning-python/decision_tree/data/test.csv", labels, ",")

    # 训练
    dtree.train()

    # 保存模型
    dtree.storeTree(dtree.tree, "test.model")

    # 画图
    tp.createPlot(dtree.tree)

    # 读取模型
    model = dtree.grabTree("test.model")
    print(json.dumps(model, ensure_ascii=False))

    # 解释
    tx = TreeExplain()
    tx.explain(model)
    for info in tx.getRes():
        print(info)

    # 预测
    vector = ['FALSE', 'UPDATE', 'IE', 'ActiveX', 'Spark']
    print("决策树输出" + dtree.predict(dtree.tree, labels, vector))
