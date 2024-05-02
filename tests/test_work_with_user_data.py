import datetime

import httpx
from jsonschema import validate
from core.contracts import CREATED_USER_SCHEM
import allure

BASE_URL = 'https://reqres.in/api/users'


def test_create_user_with_name_and_job():
    body = {
        "name": "morpheus",
        "job": "leader"
    }

    responce = httpx.post(BASE_URL, json=body)
    responce_json = responce.json()
    current_date = str(datetime.datetime.utcnow())
    creation_date = responce_json['createdAt'].replace('T', ' ')

    assert responce.status_code == 201

    validate(responce_json, CREATED_USER_SCHEM)
    assert responce_json['name'] == body['name'], "Имя не совпадает с ожидаемым"
    assert responce_json['job'] == body['job'], "Профессия не совпадает с ождиаемой"
    assert creation_date[0:16] == current_date[0:16]

    print(creation_date)
    print(current_date)
