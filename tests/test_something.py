import requests


from configurations import SERVICE_URL

from src.enums.global_enums import GlobalErrorMessages
from src.baseclasses.response import Response
from src.schemas.post import POST_SCHEMA
from src.pydantic_schemas.post import Post

def test_getting_posts():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)
    # response.assert_status_code(200).validate(POST_SCHEMA)
    response.assert_status_code(200).validate(Post)

    # received_posts = response.json()
    # print(received_posts)
    # assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    # assert len(received_posts) == 3, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value

    # for item in received_posts:
    #     validate(item, POST_SCHEMA)

# [{'id': 1, 'title': 'Post 1'}, {'id': 2, 'title': 'Post 2'}, {'id': 3, 'title': 'Post 3'}]
