#!/usr/bin/env python3
# coding:utf8

import requests
import settings

from auth import CotohaAuth


class TokenizerCommon:
    def __init__(self, _text: str, _api_base_url: str, _headers: dict):
        # input data
        self.text = _text
        self.api_base_url = _api_base_url
        self.headers = _headers

        # analyzed data
        self.response = {}

    def request_api(self):
        '''
        parse text by cotoha server
        '''

        res = requests.post(
            self.api_base_url + 'nlp/v1/parse',
            headers=self.headers,
            json={'sentence': self.text}
        )

        if res.status_code == 200:
            try:
                self.response = res.json()['result']
            except KeyError:
                print('No result is in a response.')
        else:
            raise ConnectionError(res.status_code)

    def get_tokens(self) -> list:

        if len(self.response) > 0:
            return [result['tokens'][0] for result in self.response['result']]
        else:
            raise ValueError('Use this method by doing request_api method')


class Tokenizer(TokenizerCommon):

    def __init__(self, _cotoha_auth: CotohaAuth, _text: str):

        self.access_token = _cotoha_auth.access_token
        self.access_token_publish_url = _cotoha_auth.access_token_publish_url

        self.headers = {
            'Authorization': 'Bearer ' + self.access_token,
            "Content-Type": "application/json;charset=UTF-8",
        }

        super().__init__(_text, self.api_base_url, self.headers)


class SimpleTokenizer(TokenizerCommon):

    def __init__(self, _client_id: str, _client_secret: str, _access_token_publish_url: str, _text: str):

        # auth
        self.auth_info = CotohaAuth(client_id=_client_id, client_secret=_client_secret,
                                    access_token_publish_url=_access_token_publish_url)
        self.api_base_url = 'https://api.ce-cotoha.com/api/dev/'
        self.headers = {
            'Authorization': 'Bearer ' + self.auth_info.access_token,
            "Content-Type": "application/json;charset=UTF-8",
        }

        super().__init__(_text, self.api_base_url , self.headers)

        # analysed data
        self.response: dict = {}
        self.tokens: list = []


if __name__ == '__main__':
    import json

    t = SimpleTokenizer(settings.cotoha_client_id, settings.cotoha_client_secret, 'https://api.ce-cotoha.com/v1/oauth/accesstokens', '明日の六時に渋谷で夕飯を食べる')
    t.request_api()
    print(json.dumps(t.response, ensure_ascii=False, indent=2))
