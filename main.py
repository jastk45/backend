from typing import Union
from fastapi import FastAPI
from db.models.question import Form
from db.client import client
from fastapi.middleware.cors import CORSMiddleware
from pytz import timezone
from datetime import datetime

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://192.168.41.160:8080"
]


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
    form_dict = form.dict()  # Convert the Form object to a dictionary
    
    # Set the timezone to 'America/Guayaquil'
    guayaquil_tz = timezone('America/Guayaquil')
    # Get the current datetime in the 'America/Guayaquil' timezone
    new_date = datetime.now(guayaquil_tz)
    
    # Convert the datetime object to a string in the format 'YYYY-MM-DD HH:MM:SS'
    new_date_str = new_date.strftime('%Y-%m-%d %H:%M:%S')

    # Insert the date into the dictionary
    form_dict["datetime"] = new_date_str

    client.jastk45.forms.insert_one(form_dict)  # Insert the dictionary into MongoDB
    return {"message": "Form created successfully", "datetime": new_date_str}
