# -*- coding:utf-8 -*-
# @FileName :core.py
# @Author   :Deyu He
# @Time     :2022/8/25 8:49

import copy
import random
from collections.abc import Iterable

__all__ = [
    "make_cycle_iterator",
]


def make_cycle_iterator(it, shuffle=True):
    assert isinstance(it, Iterable)
    it = list(it)
    it_ = copy.deepcopy(it)
    if shuffle:
        random.shuffle(it_)
    it_ = iter(it_)
    while True:
        try:
            yield next(it_)
        except StopIteration:
            it_ = copy.deepcopy(it)
            if shuffle:
                random.shuffle(it_)
            it_ = iter(it_)


# from loguru import logger
# a = range(5)
# count_max = 15
# count = 0
# for x in make_cycle_iterator(list(a)):
#     logger.debug(x)
#     count += 1
#     if count == count_max:
#         break
# logger.info("================================")
# count = 0
# for x in make_cycle_iterator(range(5)):
#     logger.debug(x)
#     count += 1
#     if count == count_max:
#         break
