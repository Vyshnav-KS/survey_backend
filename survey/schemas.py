from pydantic import BaseModel, Field
from typing import Literal, List, Optional

# Option for a question
class QuestionOption(BaseModel):
    option_text: str 

# Question model
class Question(BaseModel):
    question_text: str
    question_type: Literal["mcq", "input", "checkbox"] = "input"
    options: Optional[List[QuestionOption]]

    class Config:
        orm_mode = True

# Survey model
class CreateSurveyRequest(BaseModel):
    title: str
    description: str
    questions: List[Question]

    class Config:
        orm_mode = True

# Answer request
class AnswerRequest(BaseModel):
    question_id: int
    answer_text: Optional[str] = None
    selected_option_id: Optional[int] = None

# Survey Response model
class CreateSurveyResponseRequest(BaseModel):
    survey_id: int
    answers: List[AnswerRequest]

    class Config:
        orm_mode = True

# Answer response
class AnswerBase(BaseModel):
    question_id: int
    answer_text: Optional[str]
    selected_option_id: Optional[int]

    class Config:
        orm_mode = True

class ResponseBase(BaseModel):
    survey_id: int
    answers: List[AnswerBase]

    class Config:
        orm_mode = True


    