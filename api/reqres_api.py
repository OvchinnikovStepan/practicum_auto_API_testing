import allure
from api.api import Api
from model.single_user_model import  ResponseSingleUserModel
from model.create_model import RequestCreateUserModel, ResponseCreateUserModel
class ReqresApi(Api):

    """URl"""
    _URL = 'https://reqres.in'

    """Endpoint"""
    _ENDPOINT = '/api/users/'

    @allure.step('Обращение к create')
    def reqres_create(self, param_request_body: RequestCreateUserModel):
        return self.post(url=self._URL,
                         endpoint=self._ENDPOINT,
                         json_body=param_request_body.to_dict())

    """Собираем респонс в объект для последующего использования"""
    def deserialize_single_user(self):
        """для метода get (single user)"""
        payload = self.get_payload([])
        return ResponseSingleUserModel(id=payload['data']['id'],
                                       email=payload['data']['email'],
                                       first_name=payload['data']['first_name'],
                                       last_name=payload['data']['last_name'],
                                       avatar=payload['data']['avatar'],
                                       url=payload['support']['url'],
                                       text=payload['support']['text'])
    
    def reqres_single_user(self, user_id: int):
        return self.get(url=self._URL,
                        endpoint=self._ENDPOINT + str(user_id))