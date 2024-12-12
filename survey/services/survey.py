from survey.models import Survey, Question, QuestionOption, ResponseTable, Answer
import survey.schemas as schemas
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

def create(request: schemas.CreateSurveyRequest, db: Session):

    new_survey = Survey(
        title = request.title,
        description = request.description,
        
    )

    for question in request.questions:
        new_question = Question(
            question = question.question_text,
            question_type = question.question_type
        )

        if question.options:
            for option in question.options:
                new_option = QuestionOption(
                    option_text = option.option_text
                )
                new_question.options.append(new_option)
        
        new_survey.questions.append(new_question)
    db.add(new_survey)
    db.commit()
    db.refresh(new_survey)

    return new_survey

def add_answer(request: schemas.CreateSurveyResponseRequest, db: Session):

    survey = db.query(Survey).filter(Survey.id == request.survey_id).first()

    if not survey:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Survey not found")
    
    response = ResponseTable(survey_id = request.survey_id)
    db.add(response)
    db.flush() # Get the response.id before committing


    for answer_data in request.answers:
        question = db.query(Question).filter(Question.id == answer_data.question_id).first()
        if not question or question.survey_id != request.survey_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid question ID: {answer_data.question_id}"
            )
        if question.question_type in ["mcq", "checkbox"]:
            if not answer_data.selected_option_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Selected option required for question ID: {answer_data.question_id}"
                )
            option = db.query(QuestionOption).filter(QuestionOption.id == answer_data.selected_option_id).first()
            if not option or option.question_id != question.id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Invalid option ID: {answer_data.selected_option_id}"
                )

        # Create the answer entry
        answer = Answer(
            response_id=response.id,
            question_id=answer_data.question_id,
            answer_text=answer_data.answer_text,
            selected_option_id=answer_data.selected_option_id
        )
        db.add(answer)

    # Commit all changes
    db.commit()

    return {"message": "Response saved successfully"}

def get_survey_response(survey_id: int, db: Session):
    survey = db.query(Survey).filter(Survey.id == survey_id).first()

    if not survey:
        raise HTTPException(status_code=404, detail="Survey not found")

    # Query the responses related to this survey
    responses = db.query(ResponseTable).filter(ResponseTable.survey_id == survey_id).all()

    if not responses:
        raise HTTPException(status_code=404, detail="No responses found for this survey")

    # Map the responses to the schema
    response_data = []
    for response in responses:
        answers = []
        for answer in response.answers:
            answers.append({
                "question_id": answer.question_id,
                "answer_text": answer.answer_text,
                "selected_option_id": answer.selected_option_id
            })
        response_data.append({
            "survey_id": survey_id,
            "answers": answers
        })

    return response_data

    
