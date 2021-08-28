#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/28 4:29 PM
# @Author : Erwin
import tensorflow as tf
import numpy as np
import random

# # ================================== 创建 TensorSliceDataset ======================================
# b = {"a": np.array([1.0, 2.0, 3.0, 4.0, 5.0]),
#      "b": np.random.uniform(size=(5, 2))}
#
# dataset = tf.data.Dataset.from_tensor_slices(b)
#
# iterator = dataset.make_one_shot_iterator()
# one_element = iterator.get_next()
# with tf.Session() as sess:
#     for i in range(5):
#         print(sess.run(one_element))
#
# # ================================== tf.argmax ======================================
# logits = tf.constant([2, 20, 30, 3, 6])
# predicted_classes = tf.argmax(logits)
# with tf.Session() as sess:
#     print(sess.run(predicted_classes))
#
# logits = tf.constant([[2], [20], [30], [3], [6]], 1)
# predicted_classes = tf.argmax(logits)
# with tf.Session() as sess:
#     print(sess.run(predicted_classes))

# ================================== tf.reshape demo1======================================
# 参考：https://zhuanlan.zhihu.com/p/51162209
x = tf.placeholder('float')
# y = tf.reshape(x, [-1, 4, 4, 1])
y = tf.reshape(x, [2, -1])

# with tf.Session() as sess:
#     x1 = np.asarray([random.uniform(0, 1) for i in range(32)])
#     result = sess.run(y, feed_dict={x: x1})
#     print(result)
#
# # ================================== tf.reshape demo2======================================
# x = tf.constant([[1, 2], [3, 4]])
# y = tf.reshape(x, [-1])
# with tf.Session() as sess:
#     print(sess.run(y))

# # ================================== tf.reshape demo2======================================
# x = tf.ones((2, 2, 2))
# y = x[:, tf.newaxis]
# print(x)
# print(y.shape)
#

# # ================================== tf.string demo======================================
value = ["a,b"]
y = tf.string_split(value, delimiter=',')
with tf.Session() as sess:
    print(sess.run(y))

# # ================================== tf.string demo======================================
# tf.enable_eager_execution()
# print (tf.string_split(['this is example sentence']).values)

# # ================================== sigmoid demo======================================
# """
# 记录两点：
# 1. dtype=tf.float32 不写会遇到侧错，解决参考：https://stackoverflow.com/questions/44417133/typeerror-value-passed-to-parameter-a-has-datatype-not-in-list-of-allowed-val/44417286
# 2. how to convert logits to probability in binary classification in tensorflow?：https://stackoverflow.com/questions/46416984/how-to-convert-logits-to-probability-in-binary-classification-in-tensorflow
# """
# logit = tf.constant([-0.1, 2, 3, 4], dtype=tf.float32)
# # prediction = tf.round(tf.nn.sigmoid(logit))
# prediction_softmax = tf.nn.softmax(logit)
# prediction_sigmoid = tf.nn.softmax(logit)
# with tf.Session() as sess:
#     print(sess.run(prediction_softmax))
#     print(sess.run(prediction_sigmoid))
#     print(sess.run(tf.round(tf.nn.sigmoid(logit))))
#     print(sess.run(tf.nn.sigmoid(logit)))
#     print(sess.run(tf.identity(tf.nn.sigmoid(logit), name="rank_predict")))
