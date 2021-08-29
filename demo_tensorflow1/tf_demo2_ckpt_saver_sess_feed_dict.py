#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/28 4:25 PM
import tensorflow as tf

"""
占位符的 Saver 保存示例
"""
model_name = "./model_save/tf_demo2_ckpt_saver_sess_feed_dict/model.ckpt"


def feed_dict_save():
    """
    记录两点：
    1. TF 中占位符、以及feed_dict 用法。
    2. TF 中模型 checkpoint 方式的模型保存
    """
    w1 = tf.placeholder(dtype=tf.float32, name='w1')
    w2 = tf.placeholder(dtype=tf.float32, name='w2')
    b1 = tf.Variable(2.0, name='bias')
    feed_dict = {w1: 4, w2: 8}

    w3 = tf.add(w1, w2)
    w4 = tf.multiply(w3, b1, name='op_to_restore')
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        # print(sess.run(w4, feed_dict))
        sess.run(w4, feed_dict)
        saver.save(sess, model_name, global_step=1000)


feed_dict_save()