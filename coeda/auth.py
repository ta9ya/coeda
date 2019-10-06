#!/usr/bin/env python
# -*- encoding:utf-8 -*-


# -*- coding:utf-8 -*-

import requests


class CotohaAuth:

    def __init__(self, client_id: str, client_secret: str, access_token_publish_url: str, access_token: str = None):
        '''
        :param client_id: cotoha client id
        :param client_secret: cotoha client secret
        :param access_token_publish_url: cotoha access token url
        :param access_token:
        '''

        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token_publish_url = access_token_publish_url

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

        response = requests.post(self.access_token_publish_url, headers=headers, json=data)

        if response.json().get('access_token'):
            return response.json()['access_token']
        else:
            raise ValueError(response.json())
