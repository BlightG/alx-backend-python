#!/usr/bin/env python3
""" a module for testing the functions of the utils module """
import unittest
from parameterized import parameterized
from typing import List, Mapping, Sequence, Any, Dict
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

    @patch('client.get_json')
    def test_public_repos_url(self, mock_get_json: Any):
        """ mocks the org function to test the public repos property """
        mock_get_json.return_value = {"repos_url": "name"}
        organ = GithubOrgClient('google')
        self.assertEqual(organ._public_repos_url, "name")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: Any):
        """ tests public repos """
        mock_get_json.return_value = [{"name": "google",
                                      "license": {"key": "repo_key"}}]
        with patch("client.GithubOrgClient._public_repos_url")\
        as mock_public_repo:
            mock_public_repo.return_value = {"name": "google"}
            organ = GithubOrgClient('google')
            self.assertEqual(organ.public_repos("repo_key"), ["google"])
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict[str, Dict],
                         license: str, response: str):
        """ tests the has licince function """
        organ = GithubOrgClient('google')
        self.assertEqual(organ.has_license(repo, license), response)
