#!/usr/bin/env python3
""" a module to wrap math.floor with type annotation """
import math


def floor(n: float) -> int:
    """ a type wraped floor function """
    return math.floor(n)
