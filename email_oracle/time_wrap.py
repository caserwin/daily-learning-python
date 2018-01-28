#!/usr/bin/env python

from __future__ import print_function
from functools import wraps
import datetime


def timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        result = function(*args, **kwargs)
        print()
        return result
    return function_timer