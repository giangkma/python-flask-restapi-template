from app.api.business.common import findById
from app.api.exceptions.questions import QuestionNotFound
from app.model.questions import Question


def findQuestionById(id: str) -> Question:
    return findById(Question, id, QuestionNotFound)
