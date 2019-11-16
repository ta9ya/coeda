#!/usr/bin/env python3
# coding:utf8


import settings
from coeda import Tokenizer, CotohaAuth


cotoha_auth = CotohaAuth(
			settings.cotoha_client_id,
			settings.cotoha_client_secret,
			settings.cotoha_access_token_publish_url,)


def test_get_token_form():
	test_case = [('明日の六時に渋谷で夕飯を食べる', ['明日', 'の', '六時', 'に', '渋谷', 'で', '夕飯', 'を', '食べ', 'る'])]

	for query, result in test_case:
		tokenizer = Tokenizer(cotoha_auth, query)
		tokenizer.parse()
		assert tokenizer.get_token_form() == result
