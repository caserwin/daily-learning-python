#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/28 4:28 PM
# @Author : Erwin
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import tensorflow as tf
from demo_tensorflow1 import iris_data

parser = argparse.ArgumentParser()
parser.add_argument('--batch_size', default=100, type=int, help='batch size')
parser.add_argument('--train_steps', default=1000, type=int, help='number of training steps')
model_dir_ckpt = "./model_save/tf_demo5_ckpt_estimator_model_save_predict/"
"""
参考：https://github.com/tensorflow/models/blob/r1.11/samples/core/get_started/custom_estimator.py
"""

mode = "train"
# Permanently changes the pandas settings
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

def my_model(features, labels, mode, params):
    """DNN with three hidden layers, and dropout of 0.1 probability."""
    # Create three fully connected layers each layer having a dropout
    # probability of 0.1.
    net = tf.feature_column.input_layer(features, params['feature_columns'])
    logging_hook = tf.train.LoggingTensorHook(tensors={
        "SepalLength": features.get("SepalLength"),
        "size": tf.size(features.get("SepalLength")),
        "net": net
    }, every_n_iter=10)
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
            'test': tf.constant(['Hello, TensorFlow!'] * 3)
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
    return tf.estimator.EstimatorSpec(mode, loss=loss, train_op=train_op, training_hooks=[logging_hook])


def main(argv):
    if mode == "train":
        args = parser.parse_args(argv[1:])
        # Fetch the data
        (train_x, train_y), (test_x, test_y) = iris_data.load_data()

        # Feature columns describe how to use the input.
        my_feature_columns = []
        for key in train_x.keys():
            my_feature_columns.append(tf.feature_column.numeric_column(key=key))

        run_config = tf.estimator.RunConfig(model_dir=model_dir_ckpt, tf_random_seed=1024, save_checkpoints_secs=30,
                                            keep_checkpoint_max=5)
        classifier = tf.estimator.Estimator(model_fn=my_model,
                                            params={'feature_columns': my_feature_columns, 'hidden_units': [10, 10],
                                                    'n_classes': 3, },
                                            config=run_config)

        # Train the Model.
        classifier.train(input_fn=lambda: iris_data.train_input_fn(train_x, train_y, args.batch_size),
                         steps=args.train_steps)

        # Evaluate the model.
        eval_result = classifier.evaluate(input_fn=lambda: iris_data.eval_input_fn(test_x, test_y, args.batch_size))
        print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))
    else:
        test_x = {
            'SepalLength': [5.1, 5.9, 6.9],
            'SepalWidth': [3.3, 3.0, 3.1],
            'PetalLength': [1.7, 4.2, 5.4],
            'PetalWidth': [0.5, 1.5, 2.1],
        }
        my_feature_columns = []
        for key in ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']:
            my_feature_columns.append(tf.feature_column.numeric_column(key=key))

        model = tf.estimator.Estimator(model_fn=my_model,
                                       params={'feature_columns': my_feature_columns, 'hidden_units': [10, 10],
                                               'n_classes': 3, })
        predictions = model.predict(input_fn=lambda: iris_data.eval_input_fn(test_x, labels=None, batch_size=100),
                                    checkpoint_path=tf.train.latest_checkpoint(model_dir_ckpt))

        # 预测输出
        for pred_dict in predictions:
            print(pred_dict)
            # template = '\nPrediction is "{}" ({:.1f}%)'
            #
            # class_id = pred_dict['class_ids'][0]
            # probability = pred_dict['probabilities'][class_id]
            # print(template.format(class_id, 100 * probability))
            # print(pred_dict['test'])


if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)
