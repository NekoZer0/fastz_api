from http import HTTPStatus

from fastapi import FastAPI

from fastz_api.schemas import Message

app = FastAPI(title='FastZ_API', version='0.1.0')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_zero():
    return {'message': 'Olá mundo antes de vc!'}
