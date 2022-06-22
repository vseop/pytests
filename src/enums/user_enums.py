from enum import Enum


class Genders(Enum):
    female = 'female'
    male = 'male'

class Statuses(Enum):

    ACTIVE = "ACTIVE"
    BANNED = "BANNED"
    DELETED = "DELETED"
    INACTIVE = "INACTIVE"
    MERGED = "MERGED"

class UserErrors(Enum):
    WRONG_EMAIL = "Email doesn't contain @"
