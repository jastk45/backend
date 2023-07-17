from typing import Union

from fastapi import FastAPI
from db.models.question import Form
from db.client import client

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/form")
def create_form(form: Form):
    # Aquí puedes guardar el formulario en tu base de datos o realizar otras operaciones
    client.jastk45.forms.insert_one({'x': 1})
    return {"message": "Form created successfully"}