#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/28 4:27 PM
# @Author : Erwin
import tensorflow as tf

"""
变量的 Saver 保存示例
"""
model_name = './model_save/tf_demo3_ckpt_saver_sess_initalize_var/model.ckpt'


def initialize_var_save():
    """
    1. initialize_all_variables 是用来初始化 w,b 的。通过Lazy机制，实际在 sess.run(init)执行。
    2. 没有W和b会报错。不然没有 variable 用于 save()。
    """
    W = tf.Variable([[1, 1, 1], [2, 2, 2]], dtype=tf.float32, name='w')
    b = tf.Variable([[0, 1, 2]], dtype=tf.float32, name='b')

    with tf.Session() as sess:
        init = tf.initialize_all_variables()   # 放在 with tf.Session() as sess 外面也是可以的
        saver = tf.train.Saver()               # 放在 with tf.Session() as sess 外面也是可以的
        # print(sess.run(init))
        sess.run(init)
        saver.save(sess, model_name, global_step=1000)


initialize_var_save()