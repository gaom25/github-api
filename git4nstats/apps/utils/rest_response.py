import json


class Response:

    def __init__(self, res):
        self.status = res.status_code
        self.headers = res.headers
        self.body = self._get_body(res)

    def _get_body(self, res):
        try:
            return res.json()
        except json.JSONDecodeError:
            return res.text
