#!/usr/bin/env python3
""" a module for testing the functions of the utils module """
import unittest
from parameterized import parameterized
from typing import List, Mapping, Sequence, Any
from unittest.mock import patch, MagicMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ a class for testing the GithubOrgClient class """
    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: Any):
        """ tests the org method """
        organ = GithubOrgClient(org_name)
        mock_get_json.return_value = {"value": 'name'}
        self.assertEqual(organ.org, {"value": 'name'})
