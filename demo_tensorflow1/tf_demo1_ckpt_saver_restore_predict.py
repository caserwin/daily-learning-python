#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/28 4:24 PM
# @Author : Erwin
import tensorflow as tf
import numpy as np

"""
涉及到：
    1. 通过 Saver.save() 保存ckpt线性模型，其中涉及占位符、变量的保存。
    2. 通过 Saver.restore() 恢复ckpt模型，并且做预测。
    3. 通过 import_meta_graph 方式，恢复模型，并且做预测。
"""
global_step = 1000
_model_path = './model_save/tf_demo1_ckpt_saver_restore_predict/model.ckpt'


def save_model(model_path):
    """
    1. x_input，x_reshape，w, conv 都是占位符，属于TF 结构图中的一部分。必须先申明。
    2. 具体变量值都是通过 global_variables_initializer 初始化的。
    """
    x_input = tf.placeholder(tf.float32, shape=[7, 7], name="x_input")
    x_reshape = tf.reshape(x_input, shape=[-1, 7, 7, 1], name='x_reshape')
    w = tf.Variable(tf.truncated_normal(shape=[3, 3, 1, 5], stddev=0.1), name='w')
    conv = tf.nn.conv2d(x_reshape, w, [1, 1, 1, 1], padding="SAME", name='conv')

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        # print(sess.run(conv, feed_dict={x_input: np.random.rand(7, 7)}))
        sess.run(conv, feed_dict={x_input: np.random.rand(7, 7)})
        saver.save(sess, model_path, global_step=global_step)


def restore_model(model_path):
    """
    1. x_input、x_reshape、w、conv 必须要有，因为占位符是TF模型图结构的一部分，加载模型就是加载图结构。而不是加载变量。
    """
    # 1. 先构建结构图，否则在后续恢复时会报错。
    x_input = tf.placeholder(tf.float32, shape=[7, 7], name="x_input")
    x_reshape = tf.reshape(x_input, shape=[-1, 7, 7, 1], name='x_reshape')
    w = tf.Variable(tf.truncated_normal(shape=[3, 3, 1, 5], stddev=0.1), name='w')
    conv = tf.nn.conv2d(x_reshape, w, [1, 1, 1, 1], padding="SAME", name='conv')

    # 2. 定义输入占位符的值，用于填充占位符
    x_data = np.random.rand(7, 7)
    with tf.Session() as sess:
        saver = tf.train.Saver()
        # 3. 恢复模型
        saver.restore(sess, model_path)

        # 4. 预测
        conv_r = sess.run('conv:0', feed_dict={'x_input:0': x_data})
        print(conv_r)


def restore_model_with_mata_graph(model_path):
    """
    1. 通过 import_meta_graph 方式加载Saver 保存的ckpt 模型。
    2. 其实 import_meta_graph 也可以加载 savedmodelbuilder 保存的模型
    """

    # 1. 构建占位符变量
    x_data = np.full((7, 7), 10)
    with tf.Session() as sess:
        # 2. 恢复结构图和变量
        saver = tf.train.import_meta_graph(_model_path + "-" + str(global_step) + '.meta')
        saver.restore(sess, model_path + "-" + str(global_step) )

        # 3. 获取图
        graph = tf.get_default_graph()

        # 4. 获取占位符输入的tensor ，需要用 x_data 填充
        input_tensor = graph.get_tensor_by_name('x_input:0')
        conv_tensor = graph.get_tensor_by_name('conv:0')

        # 5. 预测
        conv_r = sess.run(conv_tensor, feed_dict={input_tensor: x_data})
        print(conv_r)


if __name__ == '__main__':
    # 'mode_save' or 'mode_restore' or 'mode_restore_with_meta_graph'
    mode = 'mode_save'
    if mode == 'mode_save':
        save_model(_model_path)
    if mode == 'mode_restore':
        restore_model(_model_path)
    if mode == 'mode_restore_with_meta_graph':
        restore_model_with_mata_graph(_model_path)

