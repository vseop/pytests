import pytest
import requests

from configurations import SERVICE_URL
from src.baseclasses.response import Response
from src.schemas.user import User


def test_getting_users_list(make_number, get_users, get_number, calculate):
    test_object = Response(get_users)
    test_object.assert_status_code(200).validate(User)
    # print(get_number)
    # print(calculate)
    # print(calculate(1, 1))
    # print(make_number)


@pytest.mark.production
@pytest.mark.skip('[ISSUE-23414]')
def test_another():
    assert 1 == 1


@pytest.mark.development
@pytest.mark.production
def test_another_failing_t():
    assert 2 == 2


@pytest.mark.production
@pytest.mark.development
@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3),
    (-1, -2, -3),
    (-1, 2, 1),
    ('b', -2, None),
    ('b', 'a', None)
])
def test_calculation(first_value, second_value, result, calculate):
    assert calculate(first_value, second_value) == result
