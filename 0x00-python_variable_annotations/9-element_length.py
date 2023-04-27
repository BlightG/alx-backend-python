#!/usr/bin/env python3
""" a module containing the below function """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ example function """
    return [(i, len(i)) for i in lst]
