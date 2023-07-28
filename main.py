from typing import List, Optional
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from pytz import timezone
import base64
from db.models.question import Question
from db.client import client

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://192.168.111.160:8000"
]

class Form(BaseModel):
    form_name: str
    questions: List[Question]
    latitude: float
    longitude: float
    datetime: str  # Cambia esto a str
    photo: Optional[List[str]] = None

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/form")
def create_form(form: Form):
    form_dict = form.dict()
    print('hola')
    # Set the timezone to 'America/Guayaquil'
    guayaquil_tz = timezone('America/Guayaquil')

    # Get the current datetime in the 'America/Guayaquil' timezone
    new_date = datetime.now(guayaquil_tz)
    
    # Convert the datetime object to a string in the format 'YYYY-MM-DD HH:MM:SS'
    new_date_str = new_date.strftime('%Y-%m-%d %H:%M:%S')

    if form_dict.get('photo'):
        for i, photo in enumerate(form_dict['photo']):
            photo_data = base64.b64decode(photo)
            with open(f'photo{i}.jpg', 'wb') as f:  # Guarda los datos decodificados como 'photo{i}.jpg'
                f.write(photo_data)

    # Insert the date into the dictionary
    form_dict["datetime"] = new_date_str

    client.jastk45.forms.insert_one(form_dict)  # Insert the dictionary into MongoDB
    return {"message": "Form created successfully", "datetime": new_date_str}
