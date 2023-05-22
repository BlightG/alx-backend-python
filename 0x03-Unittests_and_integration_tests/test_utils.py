#!/usr/bin/env python3
""" a module for testing the functions of the utils module """
from typing import List, Mapping, Sequence, Any
from parameterized import parameterized
import unittest
from unittest.mock import patch, MagicMock
from utils import (
    get_json,
    access_nested_map,
    memoize,
)



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
        """ testes error raised from access nested map """
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
        """ tests get_json fucniton from utils """
        requests.return_value.json.return_value = test_payload
        self.assertEqual(get_json(url), test_payload)


class TestMemoize(unittest.TestCase):
    """ a class for testing the memoize funciton """

    def test_memoize(self):

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        @patch('TestClass.a_property')
        def test_mock(self, mock_memo: Any):
            testcase = TestCase()
            self.assertEqual(testcase.a_method(), 42)
            self.assertEqual(testcase.a_method(), 42)
            mock_memo.assert_called_once()
