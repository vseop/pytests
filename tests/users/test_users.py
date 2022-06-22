import requests

from configurations import SERVICE_URL
from src.baseclasses.response import Response
from src.schemas.user import User


def test_getting_users_list(make_number, get_users, get_number, calculate):
    test_object = Response(get_users)
    test_object.assert_status_code(200).validate(User)
    print(get_number)
    print(calculate)
    print(calculate(1, 1))
    print(make_number)


def test_another():
    assert 1 == 1
