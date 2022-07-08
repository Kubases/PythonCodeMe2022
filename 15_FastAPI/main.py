from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()
app.counter = 0


class Product(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    code: str


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
def hello_name(name: str):
    return f"Hello {name}!"


@app.get("/counter")
def counter():
    app.counter += 1
    return f'counter: {app.counter}'


@app.post('/product')
def create_item(product: Product):
    return product


@app.get('/method')
def method_get():
    return {'method: GET'}


@app.post('/method')
def method_post():
    return {'method: POST'}

