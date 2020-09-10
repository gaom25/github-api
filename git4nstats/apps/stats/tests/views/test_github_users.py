from unittest.mock import patch

import pytest
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.test import APIClient


@pytest.mark.django_db(transaction=True)
class TestUserAuth:
    ENDPOINT = '/github-users/'

    def test_bad_request(self):

        request_data = {}
        client = APIClient()
        expected_response = {
           "errors": [
            {
                "message": "This field is required.",
                "code": "required",
                "field": "github_users"
            }
            ]
        }
        response = client.post(self.ENDPOINT, data=request_data)

        assert response.status_code == HTTP_400_BAD_REQUEST
        assert response.json() == expected_response

    @patch('github.connector.User.get')
    @patch('github.connector.Gists.get')
    @patch('github.connector.Events.get')
    def test_success_request(self, m_get_events, m_get_gists, m_get_user):
        m_get_events.return_value = [
            {
                'id': '12341',
                'type': 'type',
                'created_at': '2020-08-28T22:24:16Z'
            },
            {
                'id': '12342',
                'type': 'type',
                'created_at': '2020-08-28T22:24:16Z'
            },
            {
                'id': '12343',
                'type': 'type',
                'created_at': '2020-08-28T22:24:16Z'
            },
            {
                'id': '12344',
                'type': 'type',
                'created_at': '2020-08-28T22:24:16Z'
            },
            {
                'id': '12345',
                'type': 'type',
                'created_at': '2020-08-28T22:24:16Z'
            }
        ]
        m_get_gists.return_value = [
            {
                'id': '12341',
                'description': 'a',
                'created_at': '2020-08-28T22:24:16Z'
            },
            {
                'id': '12342',
                'description': 'b',
                'created_at': '2020-08-28T22:24:16Z'
            },
            {
                'id': '12343',
                'description': 'c',
                'created_at': '2020-08-28T22:24:16Z'
            }
            ]
        m_get_user.return_value = {
            'login': 'a',
            'id': '1234',
            'name': 'a',
            'created_at': '2020-08-28T22:24:16Z'
        }

        request_data = {
            "github_users": ["a"]
        }
        client = APIClient()
        response = client.post(self.ENDPOINT, data=request_data)

        expected_response = {
            'users': [
                {'user': 'a',
                 'gists': [
                     {
                         'id': '12341',
                         'description': 'a',
                         'created_at': '2020-08-28T22:24:16Z'
                     },
                     {
                         'id': '12342',
                         'description': 'b',
                         'created_at': '2020-08-28T22:24:16Z'
                     },
                     {
                         'id': '12343',
                         'description': 'c',
                         'created_at': '2020-08-28T22:24:16Z'
                     }
                 ],
                 'events': {
                     '12341': {
                         'id': '12341',
                         'type': 'type',
                         'created_at': '2020-08-28T22:24:16Z'
                     },
                     '12342': {
                         'id': '12342',
                         'type': 'type',
                         'created_at': '2020-08-28T22:24:16Z'
                     },
                     '12343': {
                         'id': '12343',
                         'type': 'type',
                         'created_at': '2020-08-28T22:24:16Z'
                     },
                     '12344': {
                         'id': '12344',
                         'type': 'type',
                         'created_at': '2020-08-28T22:24:16Z'
                     },
                     '12345': {
                         'id': '12345',
                         'type': 'type',
                         'created_at': '2020-08-28T22:24:16Z'
                     }
                 }
                 }]
        }

        assert response.status_code == HTTP_200_OK
        assert response.json() == expected_response

