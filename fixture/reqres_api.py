"""Фикстуры ReqRes API"""
import pytest
from api.reqres_api import ReqresApi

@pytest.fixture(scope="function")
def reqres_api() -> ReqresApi:
    """Коннект к ReqRes API"""
    return ReqresApi()