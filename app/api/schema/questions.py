from marshmallow import EXCLUDE, Schema, fields


class QuestionSchema(Schema):
    id = fields.String(dump_only=True, metadata={
        "description": "Id of the question"})
    question = fields.String(required=True, metadata={
        "description": "Title of the question"})
    answer = fields.List(fields.String(required=True), metadata={
        "description": "Answers of the question"})
    correctAnswer = fields.String(required=True, metadata={
        "description": "Correct answer of the question"})
    chapter = fields.String(required=False, metadata={
        "description": "Chapter of the question"})
    className = fields.String(required=True, metadata={
        "description": "Class name of the question"})


class UpdateQuestionSchema(Schema):
    question = fields.String(required=False, metadata={
        "description": "Title of the question"})
    answer = fields.List(fields.String(required=False), metadata={
        "description": "Answers of the question"})
    correctAnswer = fields.String(required=False, metadata={
        "description": "Correct answer of the question"})
    chapter = fields.String(required=False, metadata={
        "description": "Chapter of the question"})
    className = fields.String(required=False, metadata={
        "description": "Class name of the question"})


class CheckAnswerQuestionSchema(Schema):
    answer = fields.String(required=True, metadata={
        "description": "Student's answer"})


class QuestionQuerySchema(Schema):
    chapter = fields.String(required=False, metadata={
        "description": "chapter of the question"})
    className = fields.String(required=False, metadata={
        "description": "class name of the question"})
    question = fields.String(required=False, metadata={
        "description": "question of the string"})
