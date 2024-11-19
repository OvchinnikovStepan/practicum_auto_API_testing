"""Дата-файл для тестирования ReqRes API, single user"""
# -*- coding: utf-8 -*-
from model.single_user_model import ResponseSingleUserModel

# эталонные модели данных для проверки в тестах
# user_id = 2
user_id_2 = ResponseSingleUserModel(id=2, email='janet.weaver@reqres.in', first_name='Janet',
                                    last_name='Weaver', avatar='https://reqres.in/img/faces/2-image.jpg',
                                    url='https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral', 
                                    text='Tired of writing endless social media content? Let Content Caddy generate it for you.')

# user_id = 3
user_id_3 = ResponseSingleUserModel(id=3, email='emma.wong@reqres.in', first_name='Emma',
                                    last_name='Wong', avatar='https://reqres.in/img/faces/3-image.jpg',
                                    url='https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral', 
                                    text='Tired of writing endless social media content? Let Content Caddy generate it for you.')

# Валидные данные для тестов ('user_id', 'expected_data')
data = ((2, user_id_2), (3, user_id_3))

# пустое тело ответа
empty_data = {}

# Невалидные данные для тестов ('user_id', 'expected_data')
not_valid_data = ((129398274923874, empty_data),
                  ('test', empty_data),
                  ('роывора', empty_data))