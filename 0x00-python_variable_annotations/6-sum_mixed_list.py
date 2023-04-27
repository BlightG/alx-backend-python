#!/usr/bin/env python3
""" a module contating the function sum_mixed_type """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ accepts a mixed list of int and float and returns a sum as float """
    i: float = 0
    for j in mxd_lst:
        i += j
    return i
