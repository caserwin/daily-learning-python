# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 下午2:54
# @Author  : yidxue
from __future__ import print_function
import logging
import sys
import numpy as np

try:
    from pathlib import Path
except ImportError:
    try:
        from pathlib2 import Path  # For Python2
    except ImportError:
        raise ImportError("No pathlib or pathlib2 found")
from dtaidistance import dtw_weighted as dtww
from dtaidistance import dtw_visualisation as dtwvis
from dtaidistance import dtw
from dtaidistance.util import prepare_directory

logger = logging.getLogger("be.kuleuven.dtai.distance")
directory = None


def test_distance1():
    directory = prepare_directory()

    s1 = np.array([0., 0, 1, 2, 1, 0, 1, 0, 0, 2, 1, 0, 0])
    s2 = np.array([0., 1, 2, 3, 1, 10, 1, 0, 2, 1, 0, 0, 0])
    d, paths = dtw.warping_paths(s1, s2)
    print(d, "\n")
    # dtwvis.plot_warpingpaths(s1, s2, paths, filename=directory / "temp1.png")

    weights = np.full((len(s1), 8), np.inf)
    weights[:, 2:4] = 0.0
    weights[4:7, 2:4] = 10.0
    weights[:, 4:6] = 0.0
    weights[4:7, 4:6] = 10.0

    print(weights)
    d, paths = dtww.warping_paths(s1, s2, weights)
    print(d, "\n")
    # dtwvis.plot_warpingpaths(s1, s2, paths, filename=directory / "temp2.png")


if __name__ == "__main__":
    # Print options
    np.set_printoptions(precision=2)
    # Logger options
    logger.setLevel(logging.DEBUG)
    sh = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(message)s')
    sh.setFormatter(formatter)
    logger.addHandler(sh)
    logger.propagate = 0
    # Output path
    directory = Path(__file__).resolve().parent.parent / "tests" / "output"
    # Functions
    test_distance1()
    # test_distance2()
    # test_distance3()
    # test_distance4()
    # test_distance5()
    # test_distance6()
    # test_distance7()
