#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/19 下午2:04
# @Author : Erwin
import pickle


class RenameUnpickler(pickle.Unpickler):
    """
    https://stackoverflow.com/questions/27732354/unable-to-load-files-using-pickle-and-multiple-modules
    """

    def find_class(self, module, name):
        if name == 'HierarchicalHelper':
            from common.pickle_test.hierarchical_helper import HierarchicalHelper
            return HierarchicalHelper
        if name == 'TreeNode':
            from common.pickle_test.hierarchical_helper import TreeNode
            return TreeNode
        if name == 'ClusterHelper':
            from common.pickle_test.hierarchical_helper import ClusterHelper
            return ClusterHelper
        return super(RenameUnpickler, self).find_class(module, name)


def store_model(model, filename):
    fw = open(filename, 'wb')
    # 对象持久化包
    pickle.dump(model, fw)
    fw.close()


def read_model(filename):
    fr = open(filename, 'rb')
    print("load model {filename}".format(filename=filename))
    try:
        return pickle.load(fr, encoding='latin1')
    except ModuleNotFoundError:
        return RenameUnpickler(fr).load()
    except:
        return pickle.load(fr)


if __name__ == '__main__':
    tree_helper = read_model("/Users/cisco/workspace/mygit/daily-learning-python/common/pickle_test/tree_helper.model")

    print(tree_helper.root, tree_helper.root.isLeaf())
    print(tree_helper.root.left_node, tree_helper.root.left_node.isLeaf())
    print(tree_helper.root.right_node, tree_helper.root.right_node.isLeaf())
