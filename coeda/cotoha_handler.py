#!/usr/bin/env python3
# coding:utf8

import json
import requests

from typing import List, Dict

# from coeda import CotohaAuth
# from .cotoha_helper import Chunk, Token


class TokenizerCommon:
    def __init__(self, _text: str, _parsed: List, _chunks: List, _tokens: List):

        # input data
        self.text = _text

        # analyzed data
        self.parsed = _parsed
        self.chunks = _chunks
        self.tokens = _tokens

    def __str__(self):
        return json.dumps(self.parsed, ensure_ascii=False)

    def __repr__(self):
        return self.__str__()

    def get_token_form(self) -> List:

        if len(self.tokens) > 0:
            return [token.form for token in self.tokens]
        else:
            raise ValueError('Use this method by doing parse method')

    def contained_tokens(self, _text: str) -> List[Dict]:
        return [token for token in self.tokens if token['form'].find(_text) >= 0]

    def contained_chunks(self, _text: str) -> List[Dict]:
        return [chunk for chunk in self.chunks for token in chunk['tokens']
                if token['form'].find(_text) >= 0]


class Tokenizer(TokenizerCommon):

    access_token: str = ''
    api_base_url: str = 'https://api.ce-cotoha.com/api/dev/'

    def __init__(self, _text: str):
        """
        Args:
            text (str): analysis text
        """

        self.headers = {
            'Authorization': 'Bearer ' + Tokenizer.access_token,
            'Content-Type': 'application/json;charset=UTF-8',
        }

        _parsed = self.parse(_text)

        _chunks = [chunk for chunk in _parsed]
        _tokens = [token for chunk in _parsed for token in chunk['tokens']]

        super().__init__(_text, _parsed, _chunks, _tokens)

    def parse(self, _text: str) -> List:
        """parse the text using cotoha

        Raises:
            ConnectionError: to cotoha server

        Returns:
            List: data parsed by cotoha
        """

        res = requests.post(
            self.api_base_url + 'nlp/v1/parse',
            headers=self.headers,
            json={'sentence': _text}
        )

        if res.status_code == 200:
            try:
                _data = res.json()['result']
            except KeyError:
                print('No result is in a parsed.')
            return _data
        else:
            raise ConnectionError(res.status_code)
