#!/usr/bin/env python3
# coding:utf8


import requests
import settings


class Tokenizer:

	def __init__(self, text):

		self.text = text
		self.tokens = []

		self.url = 'https://api.ce-cotoha.com/api/dev/'
		self.cotoha_setting = {
			'client_id': settings.cotoha_client_id,
			'client_secret': settings.cotoha_client_secret,
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

	def get_tokens(self):

		res = requests.post(
			self.url + 'nlp/v1/parse',
			headers=self.cotoha_headers,
			json={'sentence': self.text}
		)

		if res.status_code == 200:
			json_data = res.json()

			for result in json_data['result']:
				self.tokens += result['tokens']

			return True

		else:
			return False


if __name__ == '__main__':
	import json

	t = Tokenizer('明日の六時に渋谷で夕飯を食べる')
	print(t.get_tokens())
	print(json.dumps(t.tokens, ensure_ascii=False, indent=2))
