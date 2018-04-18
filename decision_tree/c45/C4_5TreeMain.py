from decision_tree.c45.C4_5Tree import *
import decision_tree.draw.treePlotter as tp

if __name__ == '__main__':
    dtree = C4_5DTree()
    labels = ["age", "revenue", "student", "credit"]
    dtree.loadDataSet("/Users/cisco/workspace/mygit/daily-learning-python/decision_tree/c45/dataset.dat", ["age", "revenue", "student", "credit"])
    dtree.train()
    print(dtree.tree)

    tp.createPlot(dtree.tree)
    # dtree.storeTree(dtree.tree, "data.tree")
    # mytree = dtree.grabTree("data.tree")
    vector = ['0', '1', '0', '0']
    print("真实输出", "no", "  ->  ", "决策树输出", dtree.predict(dtree.tree, labels, vector))

