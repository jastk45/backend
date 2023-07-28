from pydantic import BaseModel
from typing import List, Optional
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
    photo: Optional[List[str]] = None  # Nuevo campo para las fotos