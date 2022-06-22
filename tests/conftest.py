import pytest
import requests

from configurations import SERVICE_URL


@pytest.fixture  # (autouse=True, scope='session') # autouse для каждого теста
def get_users():
    response = requests.get(SERVICE_URL)
    return response
