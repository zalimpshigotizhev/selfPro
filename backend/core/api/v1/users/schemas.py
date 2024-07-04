from ninja import Schema
from django.core.exceptions import ValidationError

from pydantic import model_validator


class AuthInSchema(Schema):
    phone: str


class AuthOutSchema(Schema):
    message: str


class TokenInSchema(Schema):
    phone: str
    code: str


class TokenOutSchema(Schema):
    token: str


class RegisterInSchema(Schema):
    first_name: str
    username: str
    phone: str
    password: str
    re_password: str

    @model_validator(mode='after')
    def validation(self, values):
        print(values)
        return values
