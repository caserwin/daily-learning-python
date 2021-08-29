#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/28 4:30 PM
# @Author : Erwin
# coding: utf-8
import tensorflow as tf
from tensorflow import feature_column
from tensorflow.contrib import layers
# from tensorflow.contrib import feature_column   # 说明 feature_column 还是直接用 tensorflow.feature_column 靠谱

# ================================== numeric column + bucket column==================================
def bucketized_column_test2():
    price = {'price': [[5.], [15.], [25.], [35.]]}
    price_column = layers.real_valued_column(column_name='price')
    bucket_price = layers.bucketized_column(price_column, [10, 20, 30, 40])
    price_bucket_tensor = feature_column.input_layer(features=price, feature_columns=[bucket_price])
    with tf.Session() as session:
        # print(session.run([price_bucket_tensor]))
        print(price_bucket_tensor.eval())


bucketized_column_test2()
print('_' * 80)

# ================================== numeric column + sparse column + indicator==================================
# 示例参考：https://www.jianshu.com/p/d940cd27c057
def bucketized_column_test2():
    feature = {'sex': [["a"], ["b"], ["a"], ["b"]]}

    column_sex_bucket = tf.contrib.layers.sparse_column_with_hash_bucket(column_name="sex", hash_bucket_size=3)
    column_sex_indicator = tf.feature_column.indicator_column(column_sex_bucket)
    price_bucket_tensor = feature_column.input_layer(features=feature, feature_columns=[column_sex_indicator])
    with tf.Session() as session:
        print(session.run([price_bucket_tensor]))


bucketized_column_test2()
print('_' * 80)

# ============================ numeric column + bucket column + crossed column ============================
def bucketized_column_test2():
    feature = {
        'price': [[5.], [5.], [25.], [35.]],
        'sex': [["a"], ["a"], ["a"], ["a"]]}

    column_sex_bucket = tf.contrib.layers.sparse_column_with_hash_bucket(column_name="sex", hash_bucket_size=2)

    column_price_real = layers.real_valued_column(column_name='price')
    column_price_bucket = tf.contrib.layers.bucketized_column(column_price_real, boundaries=[10, 20, 30, 40])

    column_price_sex_cross = tf.contrib.layers.crossed_column([column_price_bucket, column_sex_bucket],
                                                              hash_bucket_size=4)
    column_price_sex_indicator = tf.feature_column.indicator_column(column_price_sex_cross)

    price_bucket_tensor = feature_column.input_layer(features=feature, feature_columns=[column_price_sex_indicator])
    with tf.Session() as session:
        tensor1 = session.run([price_bucket_tensor])
        print(tensor1)


bucketized_column_test2()
print('_' * 80)

# ============================ numeric column + bucket column + crossed column + embedding ============================
# 示例参考：https://www.jianshu.com/p/d940cd27c057
# 说明：contrib.layers.embedding_column 只支持 sparse_column_with_** 特征和 crossed_column 特征
def bucketized_column_test2():
    feature = {
        'price': [[5.], [15.], [25.], [35.]],
        'sex': [["a"], ["b"], ["a"], ["b"]]}

    sex_column = tf.contrib.layers.sparse_column_with_hash_bucket(column_name="sex", hash_bucket_size=3)

    price_column = layers.real_valued_column(column_name='price')
    price_buckets = tf.contrib.layers.bucketized_column(price_column, boundaries=[10, 20, 30, 40])

    price_sex_cross = tf.contrib.layers.crossed_column([price_buckets, sex_column], hash_bucket_size=int(1e6))
    res_tensor = tf.contrib.layers.embedding_column(price_sex_cross, dimension=8)

    price_bucket_tensor = feature_column.input_layer(features=feature, feature_columns=[res_tensor])
    with tf.Session() as session:
        session.run(tf.global_variables_initializer())
        session.run(tf.tables_initializer())
        print(session.run([price_bucket_tensor]))


bucketized_column_test2()
