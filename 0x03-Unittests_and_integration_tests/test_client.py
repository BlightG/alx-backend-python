#!/usr/bin/env python3
""" a module for testing the functions of the utils module """
import unittest
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
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
    def test_org(self, org_name: str, mock_get_json: Any) -> None:
        """ tests the org method """
        organ = GithubOrgClient(org_name)
        mock_get_json.return_value = {"value": 'name'}
        self.assertEqual(organ.org, {"value": 'name'})

    @patch('client.get_json')
    def test_public_repos_url(self, mock_get_json: Any) -> None:
        """ mocks the org function to test the public repos property """
        mock_get_json.return_value = {"repos_url": "name"}
        organ = GithubOrgClient('google')
        self.assertEqual(organ._public_repos_url, "name")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: Any) -> None:
        """ tests public repos """
        mock_get_json.return_value = [{"name": "google",
                                      "license": {"key": "repo_key"}}]
        with patch("client.GithubOrgClient._public_repos_url") as mock_p_repo:

            mock_p_repo.return_value = {"name": "google"}
            organ = GithubOrgClient('google')
            self.assertEqual(organ.public_repos("repo_key"), ["google"])
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict[str, Dict],
                         license: str, response: str) -> None:
        """ tests the has licince function """
        organ = GithubOrgClient('google')
        self.assertEqual(organ.has_license(repo, license), response)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        """Sets up class fixtures before running tests."""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Tests the `public_repos` method."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """Tests the `public_repos` method with a license."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Removes the class fixtures after running all tests."""
        cls.get_patcher.stop()
