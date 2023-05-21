#!/usr/bin/env python3
""" a module for testing the functions of the utils module """
from typing import List, Mapping, Sequence, Any
from parameterized import parameterized
import unittest
access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ a class for testing the access_nested_map funciton """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping, key:Sequence, result: Any):
        self.assertEqual(access_nested_map(nested_map, key), result)
