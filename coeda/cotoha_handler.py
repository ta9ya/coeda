#!/usr/bin/env python3
# coding:utf8

import json
import requests
import settings

from coeda import CotohaAuth
from .cotoha_helper import Chunk, Token


class TokenizerCommon:
    def __init__(self, _text: str, _api_base_url: str, _headers: dict):

        # input data
        self.text = _text
        self.api_base_url = _api_base_url
        self.headers = _headers

        # analyzed data
        self.parsed = {}
        self.chunks = []
        self.tokens = []

    def __str__(self):
        return json.dumps(self.parsed, ensure_ascii=False)

    def __repr__(self):
        return self.__str__()

    def parse(self):
        ''' parse text by cotoha server '''
        res = requests.post(
            self.api_base_url + 'nlp/v1/parse',
            headers=self.headers,
            json={'sentence': self.text}
        )

        if res.status_code == 200:
            try:
                self.parsed = res.json()['result']
                self.chunks = [Chunk(chunk) for chunk in self.parsed]
                self.tokens = [
                    Token(token) for chunk in self.parsed for token in chunk['tokens']]
            except KeyError:
                print('No result is in a parsed.')

        else:
            raise ConnectionError(res.status_code)

    def get_token_form(self) -> list:

        if len(self.tokens) > 0:
            return [token.form for token in self.tokens]
        else:
            raise ValueError('Use this method by doing parse method')


class Tokenizer(TokenizerCommon):

    def __init__(self, _cotoha_auth: CotohaAuth, _text: str):

        self.access_token = _cotoha_auth.access_token
        self.access_token_publish_url = _cotoha_auth.access_token_publish_url

        self.headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/json;charset=UTF-8',
        }

        super().__init__(_text, _cotoha_auth.api_base_url, self.headers)


class SimpleTokenizer(TokenizerCommon):

    def __init__(self, _client_id: str, _client_secret: str, _access_token_publish_url: str, _text: str):

        # auth
        self.auth_info = CotohaAuth(client_id=_client_id, client_secret=_client_secret,
                                    access_token_publish_url=_access_token_publish_url)
        self.headers = {
            'Authorization': 'Bearer ' + self.auth_info.access_token,
            'Content-Type': 'application/json;charset=UTF-8',
        }

        super().__init__(_text, self.auth_info.api_base_url, self.headers)


if __name__ == '__main__':

    t = SimpleTokenizer(settings.cotoha_client_id, settings.cotoha_client_secret,
                        'https://api.ce-cotoha.com/v1/oauth/accesstokens', '明日の六時に渋谷で夕飯を食べる')
    t.parse()
    print(json.dumps(t.parsed, ensure_ascii=False, indent=2))
    print(t.get_token_form())
