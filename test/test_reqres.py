import requests
from faker import Faker
from pytest_voluptuous import S

from data.data import user_data, CREATED, user_register, SUCCESSFUL, DELETED, register, create

faker = Faker()


def test_get_user_list():
    response = requests.get('https://reqres.in/api/users?page=2')
    assert len(response.json()['data']) == 6, 'Count of users should be 6'


def test_get_single_user():
    response = requests.get('https://reqres.in/api/users/2')
    assert response.json()['data']['id'] == 2, 'Id of user should be 2'
    assert S(register) == response.json()


def test_delete_user():
    response = requests.delete('https://reqres.in/api/users/1')
    assert response.status_code == DELETED, f'Status code should be {DELETED}'


def test_create_new_user():
    name = faker.first_name()
    job = faker.job()
    data = user_data(name, job)

    response = requests.post('https://reqres.in/api/users', data=data)
    assert response.status_code == CREATED, f'Status code should be {CREATED}'
    assert response.json()['name'] == name, f'Name should be equal {name}'
    assert response.json()['job'] == job, f'Job should be equal {job}'
    assert S(create) == response.json()


def test_register_successful():
    email = "eve.holt@reqres.in"
    password = "pistol"
    data = user_register(email, password)
    response = requests.post('https://reqres.in/api/register', data=data)

    assert response.status_code == SUCCESSFUL, f'Status code should be {SUCCESSFUL}'
    assert response.json()['id'] == 4
    assert response.json()['token'] == "QpwL5tke4Pnpja7X4"
    assert S(register) == response.json()
