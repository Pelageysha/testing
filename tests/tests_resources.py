import httpx
from jsonschema import validate
from core.contracts import RESOURCE_DATA_SCHEMA

BASE_URL = 'https://reqres.in'
LIST_RESOURCE = '/api/unknown'
SINGLE_RESOURCE = '/api/unknown/2'
UNKNOWN_RESOURCE = '/api/unknown/23'


def test_list_of_resources():
    response = httpx.get(BASE_URL + LIST_RESOURCE)
    assert response.status_code == 200

    resource_data = response.json()['data']
    for item in resource_data:
        validate(item, RESOURCE_DATA_SCHEMA)
        assert item['color'].startswith('#')


def test_single_resource():
    response = httpx.get(BASE_URL + SINGLE_RESOURCE)
    assert response.status_code == 200

    resource_data = response.json()['data']
    validate(resource_data, RESOURCE_DATA_SCHEMA)
    assert resource_data['color'].startswith('#')


def test_unknown_resource():
    responce = httpx.get(BASE_URL + UNKNOWN_RESOURCE)
    assert responce.status_code == 404

