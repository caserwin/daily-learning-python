#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/28 4:28 PM
# @Author : Erwin
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import tensorflow as tf
from pathlib import Path
from tensorflow.contrib import predictor
from demo_tensorflow1 import iris_data

parser = argparse.ArgumentParser()
parser.add_argument('--batch_size', default=100, type=int, help='batch size')
parser.add_argument('--train_steps', default=1000, type=int, help='number of training steps')
model_dir = "./model_save/tf_demo6_pb_estimator_model_save_predict/"
"""
参考：https://github.com/tensorflow/models/blob/r1.11/samples/core/get_started/custom_estimator.py
"""

mode = "train"


def my_model(features, labels, mode, params):
    """DNN with three hidden layers, and dropout of 0.1 probability."""
    # Create three fully connected layers each layer having a dropout
    # probability of 0.1.
    net = tf.feature_column.input_layer(features, params['feature_columns'])
    for units in params['hidden_units']:
        net = tf.layers.dense(net, units=units, activation=tf.nn.relu)

    # Compute logits (1 per class).
    logits = tf.layers.dense(net, params['n_classes'], activation=None)

    # Compute predictions.
    predicted_classes = tf.argmax(logits, 1)
    if mode == tf.estimator.ModeKeys.PREDICT:
        predictions = {
            'class_ids': predicted_classes[:, tf.newaxis],
            'probabilities': tf.nn.softmax(logits),
            'logits': logits,
        }
        return tf.estimator.EstimatorSpec(mode, predictions=predictions)

    # Compute loss.
    loss = tf.losses.sparse_softmax_cross_entropy(labels=labels, logits=logits)

    # Compute evaluation metrics.
    accuracy = tf.metrics.accuracy(labels=labels, predictions=predicted_classes, name='acc_op')
    metrics = {'accuracy': accuracy}
    tf.summary.scalar('accuracy', accuracy[1])

    if mode == tf.estimator.ModeKeys.EVAL:
        return tf.estimator.EstimatorSpec(mode, loss=loss, eval_metric_ops=metrics)

    # Create training op.
    assert mode == tf.estimator.ModeKeys.TRAIN

    optimizer = tf.train.AdagradOptimizer(learning_rate=0.1)
    train_op = optimizer.minimize(loss, global_step=tf.train.get_global_step())
    return tf.estimator.EstimatorSpec(mode, loss=loss, train_op=train_op)


def main(argv):
    if mode == "train":
        args = parser.parse_args(argv[1:])
        # Fetch the data
        (train_x, train_y), (test_x, test_y) = iris_data.load_data()

        # Feature columns describe how to use the input.
        my_feature_columns = []
        for key in train_x.keys():
            my_feature_columns.append(tf.feature_column.numeric_column(key=key))

        classifier = tf.estimator.Estimator(model_fn=my_model, params={'feature_columns': my_feature_columns,
                                                                       'hidden_units': [10, 10], 'n_classes': 3, })

        # Train the Model.
        classifier.train(input_fn=lambda: iris_data.train_input_fn(train_x, train_y, args.batch_size),
                         steps=args.train_steps)

        # Evaluate the model.
        eval_result = classifier.evaluate(input_fn=lambda: iris_data.eval_input_fn(test_x, test_y, args.batch_size))
        print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

        # 保存模型
        feature_spec = tf.feature_column.make_parse_example_spec(my_feature_columns)
        serving_input_receiver_fn = tf.estimator.export.build_parsing_serving_input_receiver_fn(feature_spec)
        classifier.export_saved_model(model_dir, serving_input_receiver_fn)
    else:
        subdirs = [x for x in Path(model_dir).iterdir() if x.is_dir() and 'temp' not in str(x)]
        latest = str(sorted(subdirs)[-1])
        predict = predictor.from_saved_model(latest)

        input = {
            'SepalLength': [5.1, 5.9, 6.9],
            'SepalWidth': [3.3, 3.0, 3.1],
            'PetalLength': [1.7, 4.2, 5.4],
            'PetalWidth': [0.5, 1.5, 2.1],
        }

        # 样本数量
        record_num = len(input.values()[0])
        examples = []
        for i in range(record_num):
            feature = {}
            for col in input.keys():
                feature[col] = tf.train.Feature(float_list=tf.train.FloatList(value=[input.get(col)[i]]))
            example = tf.train.Example(features=tf.train.Features(feature=feature))
            examples.append(example.SerializeToString())

        # 将输入数据转换成序列化后的 Example 字符串。
        predictions = predict({'examples': examples})

        # 预测输出
        print(predictions["logits"])
        print("==========================")
        print(predictions["probabilities"])
        print("==========================")
        print(predictions["class_ids"])
        print("==========================")
        print(predictions["features"])


if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)
