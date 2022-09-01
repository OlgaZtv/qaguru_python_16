from faker import Faker
from pytest_voluptuous import S

from data.data import user_data, CREATED, user_register, SUCCESSFUL, register, create
from utils.sessions import reqres

faker = Faker()


def test_get_user_list():
    response = reqres().get('/api/users?page=2')
    assert len(response.json()['data']) == 6, 'Count of users should be 6'


def test_get_single_user():
    response = reqres().get('/api/users/2')
    assert response.json()['data']['id'] == 2, 'Id of user should be 2'
    assert S(register) == response.json()


def test_single_user_not_found():
    response = reqres().get('/api/users/23')
    assert response.status_code == 404


def test_create_new_user():
    name = faker.first_name()
    job = faker.job()
    payload = user_data(name, job)

    response = reqres().post('/api/users', data=payload)
    assert response.status_code == CREATED, f'Status code should be {CREATED}'
    assert response.json()['name'] == name, f'Name should be equal {name}'
    assert response.json()['job'] == job, f'Job should be equal {job}'
    assert S(create) == response.json()


def test_register_successful():
    email = "eve.holt@reqres.in"
    password = "pistol"
    payload = user_register(email, password)
    response = reqres().post('/api/register', data=payload)

    assert response.status_code == SUCCESSFUL, f'Status code should be {SUCCESSFUL}'
    assert response.json()['id'] == 4
    assert response.json()['token'] == "QpwL5tke4Pnpja7X4"
    assert S(register) == response.json()


def test_update_user():
    name = "morpheus"
    job = "zion resident"
    payload = user_data(name, job)
    response = reqres().put('/api/users/2', data=payload)

    assert response.status_code == SUCCESSFUL, f'Status code should be {SUCCESSFUL}'