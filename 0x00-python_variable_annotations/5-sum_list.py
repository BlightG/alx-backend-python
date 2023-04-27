#!/usr/bin/env python3
""" a module holding the function sum_list """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ takes a list of floats as arugument adds them and returns a float """
    i: float = 0
    for j in input_list:
        i += j
    return i
