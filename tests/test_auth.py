#!/usr/bin/env python
# -*- encoding:utf-8 -*-


import pytest
import settings

from auth import CotohaAuth


def test_auth_normal():
    cotoha_auth = CotohaAuth(
        settings.cotoha_client_id,
        settings.cotoha_client_secret,
        settings.cotoha_access_token_publish_url
    )
    assert len(cotoha_auth.access_token) > 0


def test_auth_non_argument():
    with pytest.raises(TypeError):
        cotoha_auth = CotohaAuth()


def test_auth_miss():
    with pytest.raises(ValueError):
        cotoha_auth = CotohaAuth('a', 'b', settings.cotoha_access_token_publish_url)
