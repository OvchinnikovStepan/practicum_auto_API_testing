import allure
from api.api import Api
from model.auth import RequestAuthModel,ResponseAuthModel
class RestfulBookerApi(Api):

    """URl"""
    _URL = 'https://restful-booker.herokuapp.com'

    """Endpoint"""
    _ENDPOINT_AUTH = '/auth/'
    _ENDPOINT_BOOKING = '/booking/'

@allure.step('Обращение к auth')
def restful_auth(self, param_request_body: RequestAuthModel):
    return self.post(url=self._URL,
                     endpoint=self._ENDPOINT_AUTH,
                     json_body=param_request_body.to_dict())