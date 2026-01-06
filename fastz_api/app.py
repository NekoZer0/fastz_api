from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_zero():
    return {'message': 'Olá mundo antes de vc!'}
