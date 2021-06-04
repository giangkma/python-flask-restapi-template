from werkzeug.exceptions import HTTPException


class QuestionNotFound(HTTPException):
    code = 404
    data = {"message": "Câu hỏi không tồn tại"}
