from numpy import *
import math
import copy
import pickle


class ID3DTree(object):
    def __init__(self):  # 构造方法
        self.tree = {}  # 生成的树
        self.dataSet = []  # 数据集
        self.labels = []  # 标签集

    def loadDataSet(self, path, labels, split):
        recordlist = []
        with open(path, "r") as in_file:
            for line in in_file:
                recordlist.append(line.strip().split(split))
        self.dataSet = recordlist
        self.labels = labels

    def train(self):
        labels = copy.deepcopy(self.labels)
        self.tree = self.buildTree(self.dataSet, labels)

    def buildTree(self, dataSet, labels):
        # 抽取源数据集的决策标签列
        cateList = [data[-1] for data in dataSet]
        if cateList.count(cateList[0]) == len(cateList):
            return cateList[0]
        if len(dataSet[0]) == 1:
            return self.maxCate(cateList)
        # 核心算法
        bestFeat = self.getBestFeat(dataSet)
        bestFeatLabel = labels[bestFeat]
        tree = {bestFeatLabel: {}}
        del (labels[bestFeat])
        # 抽取最优特征轴的列向量
        uniqueVals = set([data[bestFeat] for data in dataSet])  # 去重
        for value in uniqueVals:
            # 将删除后的特征类别集建立子类别集
            subLabels = labels[:]
            # 按最优特征列和值分隔数据集
            splitDataset = self.splitDataSet(dataSet, bestFeat, value)
            subTree = self.buildTree(splitDataset, subLabels)  # 构建子树
            tree[bestFeatLabel][value] = subTree
        return tree

    # 计算出现次数最多的类别标签
    def maxCate(self, catelist):
        items = dict([(catelist.count(i), i) for i in catelist])
        return items[max(items.keys())]

    # 计算信息熵
    def computeEntropy(self, dataSet):  # 计算香农熵
        datalen = float(len(dataSet))
        cateList = [data[-1] for data in dataSet]  # 从数据集中得到类别标签
        ctList = list(set(cateList))
        # 得到类别为key、出现次数value的字典
        items = dict([(i, cateList.count(i)) for i in ctList])
        infoEntropy = 0.0
        for key in items:
            prob = float(items[key]) / datalen
            infoEntropy -= prob * math.log(prob, 2)
        return infoEntropy

    # 划分数据集；分隔数据集；删除特征轴所在的数据列， 返回剩余的数据集
    # dataSet:数据集；axis：特征轴；value：特征轴取值
    def splitDataSet(self, dataSet, axis, value):
        rtnList = []
        for featVec in dataSet:
            if featVec[axis] == value:
                rFeatVec = featVec[:axis]  # list操作：提取0 - （axis - 1）的元素
                rFeatVec.extend(featVec[axis + 1:])
                rtnList.append(rFeatVec)
        return rtnList

    # 计算最优特征
    def getBestFeat(self, dataSet):
        # 计算特征向量维，其中最后一列用于类别标签，因此要减去
        numFeatures = len(dataSet[0]) - 1  # numFeatures=4,3,3
        baseEntropy = self.computeEntropy(dataSet)
        bestInfoGain = 0.0  # 初始化最优信息增益
        bestFeature = -1  # 初始化最优特征轴
        # 外循环：遍历数据集各列，计算最优特征轴
        # i为数据集列索引：取值范围0-（numFeature - 1）
        for i in range(numFeatures):  # 抽取第i列的列向量
            uniqueVals = set([data[i] for data in dataSet])  # 去重：该列的唯一值集
            newEntropy = 0.0  # 初始化香农熵
            for value in uniqueVals:
                # 按选定列i和唯一值分隔数据集
                subDataSet = self.splitDataSet(dataSet, i, value)
                prob = len(subDataSet) / float(len(dataSet))
                newEntropy += prob * self.computeEntropy(subDataSet)
            infoGain = baseEntropy - newEntropy  # 计算最大增益
            if infoGain > bestInfoGain:
                bestInfoGain = infoGain
                bestFeature = i
        return bestFeature

    def predict(self, inputTree, featLabels, testVec):  # 分类器
        root = list(inputTree.keys())[0]
        secondDict = inputTree[root]  # value-子树结构或分类标签
        featIndex = featLabels.index(root)  # 根节点在分类标签集中的位置
        key = testVec[featIndex]
        valueOfFeat = secondDict[key]  # 易错点valueOfFeat = secondDict[key]
        print(valueOfFeat)  # {'student': {b'0': b'no', b'1': b'yes'}}
        if isinstance(valueOfFeat, dict):
            classLabel = self.predict(valueOfFeat, featLabels, testVec)  # 递归分类
        else:
            classLabel = valueOfFeat
        return classLabel

    def storeTree(self, inputTree, filename):
        fw = open(filename, 'wb')
        pickle.dump(inputTree, fw)
        fw.close()

    def grabTree(self, filename):
        fr = open(filename, 'rb')
        return pickle.load(fr)
