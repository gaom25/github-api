import logging
import requests

from typing import Any, Dict, Optional

from utils.rest_response import Response

logger = logging.getLogger(__name__)


class RESTClient:
    GET = 'get'
    PUT = 'put'
    POST = 'post'
    PATCH = 'patch'
    TIMEOUT = 60

    def __init__(
        self,
        *,
        api_url: Optional[str] = None,
        headers: Optional[Dict[str, Any]] = None
    ):

        self.api_url = api_url
        self.headers = headers or {}

    def get_request(self, *, service: str, data: Dict[str, Any]) -> Response:

        func_params = {'service': service}
        logger.info(f'get_request :: start :: {func_params}')
        return self._send_request(method=self.GET, service=service, data=data)

    def put_request(self, *, service: str, data: Dict[str, Any]) -> Response:

        func_params = {'service': service}
        logger.info(f'put_request :: start :: {func_params}')
        return self._send_request(method=self.PUT, service=service, data=data)

    def post_request(self, *, service: str, data: Dict[str, Any]) -> Response:

        func_params = {'service': service}
        logger.info(f'post_request :: start :: {func_params}')
        return self._send_request(method=self.POST, service=service, data=data)

    def patch_request(
        self,
        *,
        service: str,
        data: Dict[str, Any]
    ) -> Response:

        func_params = {'service': service}
        logger.info(f'patch_request :: start :: {func_params}')
        return self._send_request(
            method=self.PATCH,
            service=service,
            data=data
        )

    def _send_request(
        self,
        *,
        method: str,
        service: str,
        data: Dict[str, Any] = None
    ) -> Response:

        func_params = {'method': method, 'service': service}
        logger.info(f'_send_request :: start :: {func_params}')

        data = data or {}
        url = f'{self.api_url}/{service}'

        request_default_params = {
            'headers': self.headers,
            'timeout': self.TIMEOUT
        }

        if method == self.POST:
            r = requests.post(
                url,
                json=data,
                **request_default_params
            )
        elif method == self.PUT:
            r = requests.put(
                url,
                data=data,
                **request_default_params
            )
        elif method == self.PATCH:
            r = requests.patch(
                url,
                json=data,
                **request_default_params
            )
        elif method == self.GET:
            r = requests.get(
                url,
                params=data,
                **request_default_params
            )
        else:
            logger.error('_send_request :: method not allowed')
            raise AssertionError('method not allowed')

        return Response(r)
