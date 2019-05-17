#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-15 11:14
# @Author  : erwin
from collections import deque
import operator


class TreeNode(object):
    def __init__(self, idx=-1, data=None, parrent_node=None):
        self.idx = idx
        self.parrent_node = parrent_node
        self.data = data
        self.left_node = None
        self.right_node = None

    def __str__(self):
        return '<TreeNode: idx: %s, data: %s>' % (self.idx, str(self.data))

    def isLeaf(self):
        return not (self.left_node or self.right_node)


class ClusterHelper(object):
    def __init__(self, linkage_tree, len):
        self.linkage_tree = linkage_tree
        self.maxnode = linkage_tree.maxnode
        self.len = len

    def toMap(self):
        child_left, child_right, dist, cnt = self.linkage_tree.get_linkage(self.maxnode)
        node_deque = deque([(self.maxnode, child_left), (self.maxnode, child_right)])
        s = {}
        while len(node_deque) > 0:
            from_node, to_node = node_deque.popleft()
            s[to_node] = from_node
            if to_node >= self.len:
                child_left, child_right, dist, cnt = self.linkage_tree.get_linkage(to_node)
                node_deque.append((to_node, child_left))
                node_deque.append((to_node, child_right))
        return s


class HierarchicalHelper(object):
    def __init__(self, linkage_tree):
        """
        :param tree:
        linkage_tree is dtaidistance.clustering import LinkageTree
        """
        _, _, dist, cnt = linkage_tree.get_linkage(linkage_tree.maxnode)
        self.root = TreeNode(idx=linkage_tree.maxnode, data=[dist, cnt])
        self.linkage_tree = linkage_tree
        self.idx_node_map = {}
        self.buildTree(self.root, None, linkage_tree.maxnode)

    def buildTree(self, tree_node, ptree_node, idx):
        node_info = self.linkage_tree.get_linkage(idx)
        if node_info is not None:
            # 说明不是叶节点
            child_left, child_right, dist, cnt = node_info[0], node_info[1], node_info[2], node_info[3]
            if tree_node is None:
                data = [dist, cnt]
                tree_node = TreeNode(idx=idx, data=data, parrent_node=ptree_node)
                self.idx_node_map[idx] = tree_node
            # 构建左边节点
            tree_node.left_node = self.buildTree(tree_node.left_node, tree_node, child_left)
            # 构建右边节点
            tree_node.right_node = self.buildTree(tree_node.right_node, tree_node, child_right)
            return tree_node
        else:
            # 说明是叶节点：没有左右子节点和相应的数据
            tree_node = TreeNode(idx=idx, parrent_node=ptree_node)
            self.idx_node_map[idx] = tree_node
            return tree_node

    def iterTreePrint(self, node):
        if node is not None:
            print(node.idx)
            self.iterTreePrint(node.left_node)
            self.iterTreePrint(node.right_node)

    def iterTree(self, node, res_ls):
        if node.isLeaf():
            res_ls.append(node)
        else:
            self.iterTree(node.left_node, res_ls)
            self.iterTree(node.right_node, res_ls)

    def getClusterByNum(self, tree_node, num, cluster_map):
        if len(cluster_map) == 0:
            cluster_map[tree_node] = tree_node.data[0]
        if num == len(cluster_map):
            return cluster_map.keys()
        else:
            # 每次从cluster_map 选择距离最大的节点
            max_tree_node = max(cluster_map.items(), key=operator.itemgetter(1))[0]
            lmax_tree_node = max_tree_node.left_node
            rmax_tree_node = max_tree_node.right_node
            cluster_map.pop(max_tree_node)
            cluster_map[lmax_tree_node] = 0 if lmax_tree_node.isLeaf() else lmax_tree_node.data[0]
            cluster_map[rmax_tree_node] = 0 if rmax_tree_node.isLeaf() else rmax_tree_node.data[0]
            return self.getClusterByNum(tree_node, num, cluster_map)

    def getClusterByDist(self, tree_node, dist, cluster_map):
        if len(cluster_map) == 0:
            cluster_map[tree_node] = tree_node.data[0]

        min_tree_node = max(cluster_map.items(), key=operator.itemgetter(1))[0]
        if dist > cluster_map[min_tree_node]:
            return cluster_map.keys()
        else:
            # 每次从cluster_map 选择距离最大的节点
            max_tree_node = max(cluster_map.items(), key=operator.itemgetter(1))[0]
            lmax_tree_node = max_tree_node.left_node
            rmax_tree_node = max_tree_node.right_node
            cluster_map.pop(max_tree_node)
            cluster_map[lmax_tree_node] = 0 if lmax_tree_node.isLeaf() else lmax_tree_node.data[0]
            cluster_map[rmax_tree_node] = 0 if rmax_tree_node.isLeaf() else rmax_tree_node.data[0]
            return self.getClusterByDist(tree_node, dist, cluster_map)
