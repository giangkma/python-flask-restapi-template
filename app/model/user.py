from flask_mongoengine import Document
from mongoengine import ListField, StringField


class User(Document):
    role = StringField(required=True)
    score = ListField(StringField(), required=True)
    name = StringField(required=True)
    username = StringField(required=True)
    password = StringField(required=True)
