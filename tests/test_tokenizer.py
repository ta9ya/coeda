#!/usr/bin/env python3
# coding:utf8


import settings
import coeda

nlp = coeda.auth(
    settings.cotoha_client_id,
    settings.cotoha_client_secret,
    settings.cotoha_access_token_publish_url)


def test_contained_tokens():
    TESTS = [(('今日はいい天気だ',
               '今日'),
              [{'id': 0,
                'form': '今日',
                'kana': 'キョウ',
                'lemma': '今日',
                'pos': '名詞',
                'features': ['日時'],
                'dependency_labels': [{'token_id': 1,
                                       'label': 'case'}],
                'attributes': {}}],
              )]

    for t in TESTS:
        input_data = t[0]
        doc = nlp(input_data[0])
        assert doc.contained_tokens(input_data[1]) == t[1]
