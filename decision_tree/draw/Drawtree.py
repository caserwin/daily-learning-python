# coding:utf-8
import matplotlib.pyplot as plt


class DrawTree():
    # 边框样式
    decision_node = dict(boxstyle='sawtooth', fc='0.8')
    leaf_node = dict(boxstyle='round4', fc='0.8')

    # 引导线样式
    arrow_args = dict(arrowstyle='<-')

    def __init__(self, tree_data):
        self.tree_data = tree_data

        # 计算基础数据
        self.width_step = 1. / self._get_leafs_num(tree_data)  # 每个叶子的占据比例
        self.height_step = 1. / self._get_tree_depth(tree_data)  # 树的层次的占据比例

        # 坐标轴范围0~1
        self.x_off = -0.5 * self.width_step
        self.y_off = 1.

    def create_plot(self):
        # 创建图表容器
        self.fig = plt.figure(1, facecolor='white')
        self.fig.clf()
        axprops = dict(xticks=[], yticks=[])  # 去掉坐标轴
        self.sub_ax = plt.subplot(111, frameon=False, **axprops)

        # 绘制树
        self._plot_tree(self.tree_data, (0.5, 1.), '')
        plt.show()

    # 获取叶子的数量
    def _get_leafs_num(self, tree_data):
        num = 0
        for value in tree_data.values():
            if isinstance(value, dict):
                num += self._get_leafs_num(value)
            else:
                num += 1
        return num

    # 获取树的层数
    def _get_tree_depth(self, tree_data):
        max_depth = 0  # 记录同级最大的层数
        # 去掉外层的字典
        data = tree_data[list(tree_data.keys())[0]]
        for value in data.values():
            if isinstance(value, dict):
                cur_depth = 1 + self._get_tree_depth(value)
            else:
                cur_depth = 1

            if cur_depth > max_depth:
                max_depth = cur_depth
        return max_depth

    # 绘制引导线的文本
    def _plot_midtext(self, start_pt, end_pt, mid_text):
        mid_x = (end_pt[0] - start_pt[0]) / 2. + start_pt[0] - 0.03
        mid_y = (end_pt[1] - start_pt[1]) / 2. + start_pt[1]
        self.sub_ax.text(mid_x, mid_y, mid_text)

    # 节点绘制
    def _plot_node(self, node_text, start_pt, end_pt, node_type):
        self.sub_ax.annotate(node_text,
                             xy=end_pt, xycoords='axes fraction',
                             xytext=start_pt, textcoords='axes fraction',
                             va='center', ha='center', bbox=node_type, arrowprops=self.arrow_args)

    # 树绘制
    def _plot_tree(self, tree_data, end_pt, node_text):
        # 根据本节点叶子个数计算起始位置
        leaf_num = self._get_leafs_num(tree_data)
        start_pt = (self.x_off + (1. + leaf_num) / 2 * self.width_step, self.y_off)

        # 绘制分类节点
        sub_key = list(tree_data.keys())[0]
        sub_dict = tree_data[sub_key]

        self._plot_node(sub_key, start_pt, end_pt, self.decision_node)
        self._plot_midtext(start_pt, end_pt, node_text)

        self.y_off -= self.height_step  # 下一层
        for key, value in sub_dict.items():
            if isinstance(value, dict):
                self._plot_tree(value, start_pt, key)
            else:
                self.x_off += self.width_step

                # 绘制结束节点
                self._plot_node(value, (self.x_off, self.y_off), start_pt, self.leaf_node)
                self._plot_midtext((self.x_off, self.y_off), start_pt, key)
        self.y_off += self.height_step  # 上一层


if __name__ == '__main__':
    test = {'no surfacing': {0: 'no', 1: {'filppers': {0: 'no', 1: 'yes'}}}}
    # test = {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1:'yes'}}, 1:'no'}}}}
    # test = {'no surfacing':{0:'no',1:{'flippers':{ 0:'no', 1:'yes'}}, 3:'maybe'}}
    tree = DrawTree(test)
    tree.create_plot()