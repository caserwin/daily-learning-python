#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-15 14:19
# @Author  : erwin


def print_line(message):
    print("=" * 20 + message + "=" * 20)


def print_br(message):
    print(message, "\n")


def print_best_worst(scores):
    scores = sorted(scores, reverse=True)

    print("The 5 best features selected by this method are :")
    for i in range(5):
        print(scores[i][1])
    print()
    print("The 5 worst features selected by this method are :")
    for i in range(5):
        print(scores[len(scores) - 1 - i][1])