#!/usr/bin/env python3
""" a module for testing the functions of the utils module """
from typing import List, Mapping, Sequence, Any
from parameterized import parameterized
import unittest
from unittest.mock import patch, MagicMock
utils = __import__('utils')
access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json


class TestAccessNestedMap(unittest.TestCase):
    """ a class for testing the access_nested_map funciton """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               key: Sequence, result: Any):
        self.assertEqual(access_nested_map(nested_map, key), result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         Key: Sequence, error: Any):
        with self.assertRaises(error):
            access_nested_map(nested_map, Key)

class TestGetJson(unittest.TestCase):
    """ a class for testing the GetJson funciton """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, url: str, 
                      test_payload: Mapping, requests: Any):
        requests.return_value.json.return_value = test_payload
        self.assertEqual(get_json(url), test_payload)
