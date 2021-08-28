#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/28 4:30 PM
# @Author : Erwin

# coding: utf-8
import tensorflow as tf
# from tensorflow import feature_column
from tensorflow.python.feature_column import feature_column


# 1. from tensorflow.contrib import feature_column   # 说明 feature_column 还是直接用 tensorflow.feature_column 靠谱
# 2. tf.feature_column.embedding_column：支持 bucketized_column、categorical_column_with_xx、crossed_column 特征

# ================================== numeric column ==================================
def test_numeric():
    # 4行样本
    price = {'price': [[5.], [15.], [25.], [35.]]}
    price_column = feature_column.numeric_column('price', normalizer_fn=lambda x: x + 2)
    price_transformed_tensor = feature_column.input_layer(features=price, feature_columns=[price_column])
    with tf.Session() as session:
        print(session.run([price_transformed_tensor]))


test_numeric()
print('_' * 80)


# ================================== numeric column + bucket column==================================
def bucketized_column_test1():
    price = {'price': [[5.], [15.], [25.], [35.]]}
    price_column = feature_column.numeric_column('price')
    bucket_price = feature_column.bucketized_column(source_column=price_column, boundaries=[10, 20, 30, 40])
    price_bucket_tensor = feature_column.input_layer(features=price, feature_columns=[bucket_price])
    with tf.Session() as session:
        print(session.run([price_bucket_tensor]))


bucketized_column_test1()
print('_' * 80)


# ================================== numeric column + bucket column + embedding column==================================
def bucketized_column_test1():
    price = {'price': [[5.], [15.], [25.], [35.]]}
    price_column = feature_column.numeric_column('price')
    bucket_price = feature_column.bucketized_column(price_column, [10, 20, 30, 40])
    embedding_cols = tf.feature_column.embedding_column(bucket_price, dimension=3)
    net2 = feature_column.input_layer(features=price, feature_columns=embedding_cols)
    with tf.Session() as session:
        session.run(tf.global_variables_initializer())
        print(net2.eval())


bucketized_column_test1()
print('_' * 80)


# ================================== category column + bucket column + embedding==================================
def bucketized_column_test1():
    features = {'sex': [0, 1, 0, 0, 1]}

    sex = tf.feature_column.categorical_column_with_identity('sex', num_buckets=2, default_value=0)
    sex_emb = tf.feature_column.embedding_column(sex, 5, combiner='sqrtn')

    # 输入层（数据，特征列）
    inputs = tf.feature_column.input_layer(features, [sex_emb])
    with tf.Session() as session:
        session.run(tf.global_variables_initializer())
        session.run(tf.tables_initializer())
        print(session.run(inputs))


bucketized_column_test1()
print('_' * 80)


# ============================ category column + bucket column + crossed_column + embedding ============================
def bucketized_column_test1():
    features = {
        'sex': [0, 1, 0, 0, 1],
        'department': ['sport', 'sport', 'drawing', 'gardening', 'travelling'],
    }

    # 特征列
    department = tf.feature_column.categorical_column_with_vocabulary_list(
        'department', ['sport', 'drawing', 'gardening', 'travelling'], dtype=tf.string)

    sex = tf.feature_column.categorical_column_with_identity('sex', num_buckets=2, default_value=0)
    sex_department = tf.feature_column.crossed_column([department, sex], 16)
    sex_department_emb = tf.feature_column.embedding_column(sex_department, 5, combiner='sqrtn')

    # 输入层（数据，特征列）
    inputs = tf.feature_column.input_layer(features, [sex_department_emb])
    with tf.Session() as session:
        session.run(tf.global_variables_initializer())
        session.run(tf.tables_initializer())
        print(session.run(inputs))


bucketized_column_test1()
print('_' * 80)
