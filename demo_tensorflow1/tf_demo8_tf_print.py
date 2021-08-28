#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/28 4:29 PM
# @Author : Erwin
from __future__ import print_function
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0'
# os.environ['TF_CPP_MIN_VLOG_LEVEL'] = '3'

# ==================================================
# x = tf.constant([2, 3, 4, 5])
# y = tf.constant([20, 30, 40, 50])
# z = tf.add(x, y)
# with tf.Session() as sess:
#     x_, y_, z_ = sess.run([x, y, z])
#     print(x_, y_, z_)
# print('=' * 80)
# ====================== 新版写法：必须开启 .enable_eager_execution()  ============================
# import sys
#
# tf.enable_eager_execution()
# x = tf.constant([2, 3, 4, 5])
# y = tf.constant([20, 30, 40, 50])
# z = tf.add(x, y)
#
# tf.print(x, output_stream=sys.stdout)
# tf.print(z, output_stream=sys.stdout)
# print(x)
# print(z)
# print('=' * 80)
# ====================== 旧版写法：tf.enable_eager_execution() 是不能开启的 ============================
import numpy as np

x = tf.placeholder(tf.float32, [1])


def body(x):
    a = tf.constant(np.array([2]), dtype=tf.float32)
    x = a + x
    x = tf.Print(x, [x], message="test ")
    return x


def condition(x):
    return tf.reduce_sum(x) < 10


with tf.Session() as sess:
    tf.global_variables_initializer().run()
    result = tf.while_loop(cond=condition, body=body, loop_vars=[x])
    result_out = sess.run([result], feed_dict={x: np.zeros(1)})
    print(result_out)
