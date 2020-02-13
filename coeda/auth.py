#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import requests

from .cotoha_handler import Tokenizer


class CotohaAuth:

    def __init__(self, client_id: str, client_secret: str, access_token_publish_url: str, access_token: str = None):
        """create cotoha auth setting
        
        Args:
            client_id (str): cotoha client id
            client_secret (str): cotoha client secret
            access_token_publish_url (str): cotoha access token url
            access_token (str, optional): cotoha access token. Defaults to None.
        """

        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token_publish_url = access_token_publish_url
        self.api_base_url = 'https://api.ce-cotoha.com/api/dev/'

        if access_token is not None:
            self.access_token = access_token
        else:
            self.access_token = self.update_access_token()

    def update_access_token(self):
        """ update Access Token
        TODO: use Requests-OAuthlib
        """

        # if self.access_token_publish_url is not None:
        #     raise RuntimeError("access_token_publish_url is not provided.")

        headers = {"Content-Type": "application/json;charset=UTF-8"}

        data = {
            "grantType": "client_credentials",
            "clientId": self.client_id,
            "clientSecret": self.client_secret
        }

        response = requests.post(
            self.access_token_publish_url, headers=headers, json=data)

        if response.json().get('access_token'):
            return response.json()['access_token']
        else:
            raise ValueError(response.json())


def auth(client_id: str, client_secret: str, access_token_publish_url: str):
    
    headers = {"Content-Type": "application/json;charset=UTF-8"}

    data = {
        "grantType": "client_credentials",
        "clientId": client_id,
        "clientSecret": client_secret
    }

    response = requests.post(
        access_token_publish_url, headers=headers, json=data)

    if response.json().get('access_token'):
        return Tokenizer(response.json()['access_token'])
    else:
        raise ValueError(response.json())
