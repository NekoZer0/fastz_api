from http import HTTPStatus

from fastapi import FastAPI, HTTPException

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


@app.put(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def update_user(user_id: int, user: UserSchema):
    user_with_id = UserDBSchema(**user.model_dump(), id=user_id)
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuario não encontrado'
        )
    database[user_id - 1] = user_with_id
    return user_with_id


@app.delete(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuario não encontrado'
        )
    deleted_user = database.pop(user_id - 1)
    return deleted_user
