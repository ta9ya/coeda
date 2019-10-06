#!/usr/bin/env python3
# coding:utf8


import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


# setting for cotoha
cotoha_api_base_url = os.environ.get('cotoha_api_base_url')
cotoha_client_id = os.environ.get('cotoha_client_id')
cotoha_client_secret = os.environ.get('cotoha_client_secret')
cotoha_access_token_publish_url = os.environ.get('cotoha_access_token_publish_url')


# kintone = KintoneHandler(_KINTONE_TOKEN=kintone_token, app=5)
