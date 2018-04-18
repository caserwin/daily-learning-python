from decision_tree.id3.ID3Tree import *
import decision_tree.draw.treePlotter as tp


if __name__ == '__main__':
    dtree = ID3DTree()
    dtree.loadDataSet("id3/dataset.dat", ["age", "revenue", "student", "credit"])
    dtree.train()
    print(dtree.tree)

    tp.createPlot(dtree.tree)

    tp.createPlot({'age': {'1': 'yes', '2': {'credit': {'1': 'no', '0': 'yes'}}, '0': {'student': {'1': 'yes', '0': 'no'}}}})


    # tp.createPlot({'no surfacing': {0: 'no', 1: {'filppers': {0: 'no', 1: 'yes'}}}})
    #dtree.storeTree(dtree.tree, "data.tree")
    #mytree = dtree.grabTree("data.tree")

    labels = ["age", "revenue", "student", "credit"]
    vector = ['0', '1', '0', '0']
    print("真实输出", "no", "  ->  ", "决策树输出", dtree.predict(dtree.tree, labels, vector))

