from http import HTTPStatus

from fastapi import FastAPI

from fastz_api.schemas import (
    Message,
    UserDBSchema,
    UserList,
    UserPublic,
    UserSchema,
)

app = FastAPI(title='FastZ_API', version='0.1.0')

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_zero():
    return {'message': 'Olá mundo antes de vc!'}


@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_user():
    return {'users': database}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDBSchema(
        id=len(database) + 1,
        username=user.username,
        email=user.email,
        password=user.password,
    )
    database.append(user_with_id)
    return user_with_id
