"""Тест кейс для ReqRes API, single user"""
from helper.load import load_data
import allure
import pytest


pytest_plugins = ["fixture.restful_api"]
pytestmark = [allure.parent_suite("restful"),
              allure.suite("auth")]

@allure.title('Запрос на авторизацию')
@pytest.mark.parametrize(('request_params'),
                         load_data('auth_data'))
def test_auth_valid_parameters(restful_api, request_params):
    restful_api.restful_auth(request_params).status_code_should_be(200).\
        json_schema_should_be_valid('auth_schema')