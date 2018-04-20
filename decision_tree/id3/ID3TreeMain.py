from decision_tree.id3.ID3Tree import *
import decision_tree.draw.treePlotter as tp
import json

if __name__ == '__main__':
    dtree = ID3DTree()

    labels = ["ISREGISTER", "USERTYPE", "USERBROWSER", "JOINMETHOD", "SYSTEM"]
    dtree.loadDataSet("/Users/cisco/workspace/mygit/daily-learning-python/decision_tree/data/test.dat", labels, ",")

    # labels = ["ISREGISTER", "USERTYPE", "USEROS", "OSVERSION", "USERBROWSER", "BROWSERVERSION", "JOINMETHOD",
    #           "SERVICETYPE", "SERVICEID", "SITEVERSION", "COUNTRY", "PLATFORM", "SYSTEM", "ISHOST"]
    # dtree.loadDataSet("/Users/cisco/workspace/mygit/daily-learning-python/decision_tree/data/dataset.dat", labels, ",")

    # labels = ["ID", "ISREGISTER", "USERTYPE", "USEROS", "OSVERSION", "USERBROWSER", "BROWSERVERSION", "JOINMETHOD",
    #           "SERVICETYPE", "SERVICEID", "SITEVERSION", "COUNTRY", "PLATFORM", "SYSTEM", "ISHOST"]
    # dtree.loadDataSet("/Users/cisco/workspace/mygit/daily-learning-python/decision_tree/data/dataset_id.dat", labels, ",")

    dtree.train()
    print(dtree.tree)
    # print(json.dumps(dtree.tree, ensure_ascii=False))

    tp.createPlot(dtree.tree)

    # vector = ['WINDOWS', 'RETURN', 'IE', 'TRUE']
    # print("真实输出", "no", "  ->  ", "决策树输出", dtree.predict(dtree.tree, labels, vector))

    # # dtree.storeTree(dtree.tree, "data.tree")
    # # mytree = dtree.grabTree("data.tree")
