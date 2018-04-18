# # encoding: utf-8
#
# # ls = ["1	0	0	0", "1	0	0	0"]
# # recordlist = [row.strip().split("\t") for row in ls]
# # recordlist.append([1, 2, 34])
# # print(recordlist)
#
# import copy
#
#
# class ID3DTree(object):
#     def __init__(self):  # 构造方法
#         self.tree = {}  # 生成的树
#         self.dataSet = []  # 数据集
#         self.labels = []  # 标签集
#
#     def loadDataSet(self, path, labels):
#         recordlist = []
#         with open(path, "r") as in_file:
#             for line in in_file:
#                 recordlist.append(line.strip().split("\t"))
#         self.dataSet = recordlist
#         self.labels = labels
#
#     def train(self):
#         labels = copy.deepcopy(self.labels)
#         self.tree = self.buildTree(self.dataSet, labels)
#
#     def buildTree(self, dataSet, labels):
#         cateList = [data[-1] for data in dataSet]
#         print(dataSet[0])
#         if len(dataSet[0]) == 1:
#             print(self.maxCate(cateList))
#             return self.maxCate(cateList)
#         # print(cateList.count(cateList[0]))
#         # print(dataSet[0])
#
#     # 计算出现次数最多的类别标签
#     def maxCate(self, catelist):
#         items = dict([(catelist.count(i), i) for i in catelist])
#         return items[max(items.keys())]
#
# if __name__ == '__main__':
#     dtree = ID3DTree()
#     dtree.loadDataSet("dataset.dat", ["age", "revenue", "student", "credit"])
#     dtree.train()