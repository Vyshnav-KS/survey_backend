from sqlalchemy import Column, Integer, ForeignKey, String, Enum
from sqlalchemy.orm import relationship
from survey.database import Base

# Survey table
class Survey(Base):
    __tablename__ = "surveys"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)

    questions = relationship("Question", back_populates="survey")

# Questions table
class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    question = Column(String, nullable=False)
    question_type = Column(
        Enum("mcq", "input", "checkbox", name="question_type"),
        nullable=False
    )
    survey_id = Column(Integer, ForeignKey("surveys.id"))

    survey = relationship("Survey", back_populates="questions")
    options = relationship("QuestionOption", back_populates="question")

# Question options table
class QuestionOption(Base):
    __tablename__ = "question_options"

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey("questions.id"))
    option_text = Column(String, nullable=False)

    question = relationship("Question", back_populates="options")

# Response table
class ResponseTable(Base):
    __tablename__ = "responses"

    id = Column(Integer, primary_key=True)
    survey_id = Column(Integer, ForeignKey("surveys.id"))

    survey = relationship("Survey")
    answers = relationship("Answer", back_populates="response")

# Answer table
class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True)
    response_id = Column(Integer, ForeignKey("responses.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    answer_text = Column(String, nullable=True)
    selected_option_id = Column(Integer, ForeignKey("question_options.id"), nullable=True)

    response = relationship("ResponseTable", back_populates="answers")
    question = relationship("Question")
    selected_option = relationship("QuestionOption")
















 