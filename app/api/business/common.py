from typing import Type

from bson import ObjectId
from flask_mongoengine import Document
from werkzeug.exceptions import NotFound

from app.api.exceptions.common import InvalidIdException


def validateId(id: str):
    try:
        ObjectId(id)
    except Exception as ex:
        raise InvalidIdException() from ex


def findById(Modal: Type[Document], id: str, NotFoundException: Type[Exception] = NotFound) -> Document:
    validateId(id)

    result = Modal.objects(id=id)

    if not result:
        raise NotFoundException()
    return result
