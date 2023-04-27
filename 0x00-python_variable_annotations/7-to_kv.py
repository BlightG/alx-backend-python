#!/usr/bin/env python3
""" module for function to_kv """
from typing import Union, Tuple
import math


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ a function to return a tuple of k and and square of v """
    return (k, math.pow(v, 2))
