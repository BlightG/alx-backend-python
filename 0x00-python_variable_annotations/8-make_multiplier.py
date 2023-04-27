#!/usr/bin/env python3
""" a module for the function muliplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ that takes a float multiplier as argument
        and returns a function that multiplies a float by multiplier. """
    def return_multiplier(x: float) -> float:
        """ a function that multiplies multiplier by 2.22 """
        return x * multiplier
    return return_multiplier
