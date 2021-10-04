# Python+Flask RESTful template using MongoDB

![python 3.9](https://img.shields.io/badge/python-3.9-blue)
[![build](https://img.shields.io/github/workflow/status/fsjunior/python-flask-restful-mongodb-template/build)](https://github.com/fsjunior/python-flask-restful-mongodb-template/actions?query=workflow%3Abuild)
[![Codecov](https://img.shields.io/codecov/c/gh/fsjunior/python-flask-restful-mongodb-template)](https://codecov.io/gh/fsjunior/python-flask-restful-mongodb-template)
[![maintainability](https://img.shields.io/codeclimate/maintainability/fsjunior/python-flask-restful-mongodb-template)](https://codeclimate.com/github/fsjunior/python-flask-restful-mongodb-template)
[![quality gate](https://img.shields.io/sonar/quality_gate/fsjunior_python-flask-restful-mongodb-template?server=https%3A%2F%2Fsonarcloud.io)](https://sonarcloud.io/dashboard?id=fsjunior_python-flask-restful-mongodb-template)
![GitHub last commit](https://img.shields.io/github/last-commit/fsjunior/python-flask-restful-mongodb-template)

A simple and powerful 🐍+flask RESTful template with MongoDB.

## Features

- Bleeding edge [Python 3.9](https://docs.python.org/3.9/whatsnew/3.9.html) (although
  this template probably will work with older Python versions as well);
- [Flask](flask.palletsprojects.com) micro-framework;
- RESTful API with pagination and Swagger/ReDoc OpenAPI specification with [flask-smorest](https://flask-smorest.readthedocs.io/en/latest/);
- Schemas with [marshmallow](https://marshmallow.readthedocs.io/en/stable/);
- ODM with [mongoengine](http://mongoengine.org/);
- 100% code coverage tests using [pytest](https://docs.pytest.org/en/stable/)
  and [pytest-cov](https://github.com/pytest-dev/pytest-cov);
- Security analysis with [bandit](https://github.com/PyCQA/bandit);
- Continuous Integration with [github actions](https://github.com/features/actions).
- API examples.

## Getting started

After cloning this repository for your project, init the `pip` environment and install
the project dependencies:

```console
~ $ pip install -r requirements.txt
```

You will also need a `.env` file for local development and testing. You can copy the
`dotenv.test` file for this purpose.

```console
~ $ cp dotenv.test .env
```

Or you can run the template in development mode

```console
~ $ python run.py
```

Go to your browser to access the Swagger or ReDoc auto-generated docs:

```
http://127.0.0.1:8080/doc/swagger
http://127.0.0.1:8080/doc/redoc
```
