import logging

import requests

from settings.base import API_MELI

logger = logging.getLogger(__name__)


class ServiceMeli:
    def __init__(
        self,
        path: str,
        params: dict,
        endpoint: str = API_MELI,
    ):

        self.endpoint = endpoint
        self.path = path
        self.params = params

    def get(self):
        response = requests.get(self.endpoint + self.path, params=self.params)

        if response.status_code == 200:
            return response.json()

        return {"error": "fail request"}
