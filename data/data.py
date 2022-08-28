from voluptuous import Schema, ALLOW_EXTRA

DELETED = 204
CREATED = 201
SUCCESSFUL = 200

register = Schema({
    "id": int,
    "token": str
},
    extra=ALLOW_EXTRA
)

create = Schema({
    "name": str,
    "job": str,
    "id": str,
    "createdAt": str,
},
    extra=ALLOW_EXTRA
)


def user_data(name, job):
    return {
        "name": name,
        "job": job
    }


def user_register(email, password):
    return {
        "email": email,
        'password': password
    }
