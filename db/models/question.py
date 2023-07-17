from pydantic import BaseModel
from typing import List
from datetime import datetime

class Question(BaseModel):
    question_text: str
    answer: str

class Form(BaseModel):
    form_name: str
    questions: List[Question]
    latitude: float
    longitude: float
    datetime: datetime
