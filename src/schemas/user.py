from pydantic import BaseModel, validator
from src.enums.user_enums import Genders, UserErrors, StatusesUser


class User(BaseModel):
    id: int  # int=0 необязательное
    name: str
    email: str
    gender: Genders
    status: StatusesUser

    @validator('email')
    def check_that_dog_presented_in_email_address(cls, email):
        if '@' in email:
            return email
        else:
            raise ValueError(UserErrors.WRONG_EMAIL.value)
