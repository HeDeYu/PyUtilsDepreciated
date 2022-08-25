# -*- coding:utf-8 -*-
# @FileName :core.py
# @Author   :Deyu He
# @Time     :2022/8/25 8:49

import copy
import itertools
import random
from collections.abc import Iterable

__all__ = [
    "make_cycle_iterator",
]


def make_cycle_iterator(it, shuffle=True):
    assert isinstance(it, Iterable)
    if not shuffle:
        yield itertools.cycle(it)
    it_ = copy.deepcopy(it)
    random.shuffle(it_)
    it_ = iter(it_)
    while True:
        try:
            yield next(it_)
        except StopIteration:
            it_ = copy.deepcopy(it)
            random.shuffle(it_)
            it_ = iter(it_)


#
# a = [1,2,3,4,5]
# count_max = 15
# count = 0
# # for x in make_cycle_iterator(a, shuffle=False):
# for x in itertools.cycle(a):
#     print(x)
#     count += 1
#     if count == count_max:
#         break
