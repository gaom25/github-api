import os
import logging

from datetime import datetime, date
from decimal import Decimal
from typing import Any, Dict, List, Optional

from utils.rest_api import RESTClient
from utils.rest_response import Response

from github.exceptions import (
    GitHubLoanConnectionException,
    GitHubLoanException,
    GitHubPaymentConnectionException,
    GitHubPaymentException,
    GitHubLoanStatusConnectionException,
    GitHubLoanStatusException,
    GitHubOfferListConnectionException,
    GitHubOfferListException
)


logger = logging.getLogger(__name__)


class GitHubConnector(RESTClient):
    GITHUB_URL = os.getenv('GITHUB_URL')

    def __init__(self):

        assert isinstance(self.GITHUB_URL, str), (
            'GITHUB_URL must be a str instance'
        )

        super().__init__(
            api_url=self.GITHUB_URL,
        )
        self.user = User(client=self)
        self.gists = Gists(client=self)
        self.events = Events(client=self)

    def _send_request(
        self,
        *,
        method: str,
        service: str,
        data: Dict[str, Any] = None
    ) -> Response:

        try:
            response = super()._send_request(
                method=method,
                service=service,
                data=data
            )
        except Exception as exc:
            raise exc

        return response


class User:
    def __init__(self, *, client: GitHubConnector):

        assert isinstance(client, GitHubConnector), (
            'client must be a GitHubConnector instance'
        )

        self.client = client

    def get(
        self,
        *,
        user_id
    ) -> List[Dict[str, Any]]:

        service = f'users/{user_id}'

        try:
            response = self.client.get_request(
                service=service,
                data={}
            )
        except Exception as exc_info:
            logger.exception('User.get :: error on get_request')
            raise GitHubPaymentConnectionException(exc_info)

        if response.status >= 500:
            raise GitHubPaymentConnectionException(response.body)

        if response.status >= 300:
            raise GitHubPaymentException(response.body)

        if response.status == 204:
            return []

        return response.body


class Gists:
    def __init__(self, *, client: GitHubConnector):

        assert isinstance(client, GitHubConnector), (
            'client must be a GitHubConnector instance'
        )

        self.client = client

    def get(
        self,
        *,
        user_id: str
    ) -> List[Dict[str, Any]]:

        service = f'users/{user_id}/gists'
        try:
            response = self.client.get_request(
                service=service,
                data={}
            )
        except Exception as exc_info:
            logger.exception('Gists.get :: error on get_request')
            raise GitHubPaymentConnectionException(exc_info)

        if response.status >= 500:
            raise GitHubPaymentConnectionException(response.body)

        if response.status >= 300:
            raise GitHubPaymentException(response.body)

        if response.status == 204:
            return []

        return response.body


class Events:
    def __init__(self, *, client: GitHubConnector):
        assert isinstance(client, GitHubConnector), (
            'client must be a GitHubConnector instance'
        )
        self.client = client

    def get(
        self,
        *,
        user_id: str
    ) -> List[Dict[str, Any]]:

        service = f'users/{user_id}/events'
        try:
            response = self.client.get_request(
                service=service,
                data={}
            )
        except Exception as exc_info:
            logger.exception('Events.get :: error on get_request')
            raise GitHubPaymentConnectionException(exc_info)

        if response.status >= 500:
            raise GitHubPaymentConnectionException(response.body)

        if response.status >= 300:
            raise GitHubPaymentException(response.body)

        if response.status == 204:
            return []

        return response.body
