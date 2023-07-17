from pydantic import BaseModel
from typing import List

class Question(BaseModel):
    question_text: str
    answers: List[str]

class Form(BaseModel):
    form_name: str
    questions: List[Question]
