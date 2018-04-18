# coding:utf-8
import matplotlib.pyplot as plt

# 边框样式
decision_node = dict(boxstyle='sawtooth', fc='0.8')
leaf_node = dict(boxstyle='round4', fc='0.8')

# 引导线样式
arrow_args = dict(arrowstyle='<-')


# 节点绘制(画布，文本，箭头终点，箭头起点，边框样式)
def plot_node(sub_ax, node_text, start_pt, end_pt, node_type):
    sub_ax.annotate(node_text,
                    xy=end_pt, xycoords='axes fraction',
                    xytext=start_pt, textcoords='axes fraction',
                    va='center', ha='center', bbox=node_type, arrowprops=arrow_args)


if __name__ == '__main__':
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    axprops = dict(xticks=[], yticks=[])  # 去掉坐标轴
    sub_ax = plt.subplot(111, frameon=False, **axprops)

    # 绘制节点
    plot_node(sub_ax, 'a decision node', (0.5, 0.1), (0.1, 0.5), decision_node)
    plot_node(sub_ax, 'a leaf node', (0.8, 0.1), (0.3, 0.8), leaf_node)
    plt.show()