from fastapi import APIRouter, Depends
import survey.schemas as schemas
from sqlalchemy.orm import Session
from survey.database import get_db
from survey.services import survey
from typing import List

router = APIRouter()

@router.post("/survey")
def create_survey(request: schemas.CreateSurveyRequest, db: Session = Depends(get_db)):
    return survey.create(request, db)

@router.post("/answer")
def add_answer(request: schemas.CreateSurveyResponseRequest, db: Session = Depends(get_db)):
    return survey.add_answer(request, db)

@router.get("/survey/{id}/response", response_model=List[schemas.ResponseBase])
def list_response(survey_id: int, db: Session = Depends(get_db)):
    return survey.get_survey_response(survey_id, db)