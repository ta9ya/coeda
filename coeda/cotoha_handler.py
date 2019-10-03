#!/usr/bin/env python3
# coding:utf8


import requests
import settings


class Tokenizer:

	def __init__(self, _client_id: str, _client_secret: str, _text: str):

		self.text = _text
		self.response: dict = {}
		self.tokens: list = []

		self.url = 'https://api.ce-cotoha.com/api/dev/'
		self.cotoha_setting = {
			'client_id': _client_id,
			'client_secret': _client_secret,
			'access_token': 'https://api.ce-cotoha.com/v1/oauth/accesstokens'
		}

		self.token_data = {
			'grantType': 'client_credentials',
			'clientId': self.cotoha_setting['client_id'],
			'clientSecret': self.cotoha_setting['client_secret']
		}

		self.cotoha_access_token = requests.post(
			self.cotoha_setting['access_token'],
			json=self.token_data
		).json()

		self.cotoha_headers = {
			'Authorization': 'Bearer ' + self.cotoha_access_token['access_token']
		}

	def request_api(self) -> bool:

		res = requests.post(
			self.url + 'nlp/v1/parse',
			headers=self.cotoha_headers,
			json={'sentence': self.text}
		)

		if res.status_code == 200:
			self.response = res.json()
			return True

		else:
			return False

	def get_tokens(self) -> list:

		if len(self.response) > 0:
			return [result['tokens'][0] for result in self.response['result']]
		else:
			raise ValueError('Use this method by doing request_api method')


if __name__ == '__main__':
	import json

	t = Tokenizer(settings.cotoha_client_id, settings.cotoha_client_secret, '明日の六時に渋谷で夕飯を食べる')
	t.request_api()
	print(json.dumps(t.response, ensure_ascii=False, indent=2))
