from werkzeug.exceptions import HTTPException


class InvalidIdException(HTTPException):
    code = 400
    data = {"message": "ID không đúng định dạng"}
