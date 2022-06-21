import requests

from configurations import SERVICE_URL
from src.baseclasses.response import Response
from src.schemas.user import User
#
# resp = requests.get(SERVICE_URL)
# print(resp.json())
# print(resp.__getstate__())


def test_getting_users_list():
    response = requests.get(SERVICE_URL)
    test_object = Response(response)
    test_object.assert_status_code(200).validate(User)


# z = {
#   "meta": {
#     "pagination": {
#       "total": 3068,
#       "pages": 154,
#       "page": 1,
#       "limit": 20,
#       "links": {
#         "previous": "None",
#         "current": "https://gorest.co.in/public/v1/users?page\u003d1",
#         "next": "https://gorest.co.in/public/v1/users?page\u003d2"
#       }
#     }
#   },
#   "data": [
#     {
#       "id": 3260,
#       "name": "Sen. Jahnu Kaniyar",
#       "email": "kaniyar_sen_jahnu@kilback.com",
#       "gender": "male",
#       "status": "inactive"
#     },
#     {
#       "id": 3259,
#       "name": "Aslesha Gandhi",
#       "email": "gandhi_aslesha@beer.info",
#       "gender": "male",
#       "status": "active"
#     },
#     {
#       "id": 3258,
#       "name": "Sanka Tandon",
#       "email": "sanka_tandon@miller.name",
#       "gender": "male",
#       "status": "inactive"
#     },
#     {
#       "id": 3257,
#       "name": "Ranjeet Varma",
#       "email": "ranjeet_varma@welch.co",
#       "gender": "male",
#       "status": "inactive"
#     },
#     {
#       "id": 3256,
#       "name": "Saroja Johar",
#       "email": "saroja_johar@brekke.net",
#       "gender": "male",
#       "status": "inactive"
#     },
#     {
#       "id": 3255,
#       "name": "Bhudeva Rana Sr.",
#       "email": "bhudeva_rana_sr@murphy.name",
#       "gender": "female",
#       "status": "inactive"
#     },
#     {
#       "id": 3254,
#       "name": "Aanandaswarup Varman",
#       "email": "varman_aanandaswarup@brakus.io",
#       "gender": "female",
#       "status": "active"
#     },
#     {
#       "id": 3253,
#       "name": "Gautama Rana",
#       "email": "gautama_rana@schinner.info",
#       "gender": "male",
#       "status": "active"
#     },
#     {
#       "id": 3252,
#       "name": "Ms. Shakti Patel",
#       "email": "ms_shakti_patel@carroll.net",
#       "gender": "female",
#       "status": "inactive"
#     },
#     {
#       "id": 3251,
#       "name": "Gangesh Jain",
#       "email": "gangesh_jain@dach.com",
#       "gender": "female",
#       "status": "active"
#     },
#     {
#       "id": 3250,
#       "name": "Laxmi Bhat",
#       "email": "bhat_laxmi@connelly.io",
#       "gender": "female",
#       "status": "inactive"
#     },
#     {
#       "id": 3249,
#       "name": "Mangalya Gandhi",
#       "email": "gandhi_mangalya@haley.com",
#       "gender": "male",
#       "status": "inactive"
#     },
#     {
#       "id": 3248,
#       "name": "Diksha Tagore",
#       "email": "tagore_diksha@hamill.co",
#       "gender": "female",
#       "status": "inactive"
#     },
#     {
#       "id": 3245,
#       "name": "Deveshwar Patel DO",
#       "email": "do_deveshwar_patel@steuber-shields.com",
#       "gender": "male",
#       "status": "inactive"
#     },
#     {
#       "id": 3244,
#       "name": "Bhima Bhattathiri",
#       "email": "bhattathiri_bhima@maggio.co",
#       "gender": "female",
#       "status": "active"
#     },
#     {
#       "id": 3241,
#       "name": "Gov. Gajaadhar Nambeesan",
#       "email": "gajaadhar_gov_nambeesan@jacobson-watsica.net",
#       "gender": "male",
#       "status": "active"
#     },
#     {
#       "id": 3240,
#       "name": "Dhananjay Jain",
#       "email": "jain_dhananjay@jacobs.com",
#       "gender": "male",
#       "status": "inactive"
#     },
#     {
#       "id": 3239,
#       "name": "Ramaa Tagore",
#       "email": "tagore_ramaa@welch-nicolas.com",
#       "gender": "male",
#       "status": "inactive"
#     },
#     {
#       "id": 3237,
#       "name": "Daksha Mishra",
#       "email": "mishra_daksha@upton.com",
#       "gender": "female",
#       "status": "active"
#     },
#     {
#       "id": 3235,
#       "name": "Rev. Alok Iyengar",
#       "email": "alok_rev_iyengar@king-stokes.org",
#       "gender": "female",
#       "status": "inactive"
#     }
#   ]
# }

# def test_getting_posts():
#     r = requests.get(SERVICE_URL)
#     response = Response(r)
#     # response.assert_status_code(200).validate(POST_SCHEMA)
#     response.assert_status_code(200).validate(Post)

# received_posts = response.json()
# print(received_posts)
# assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
# assert len(received_posts) == 3, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value

# for item in received_posts:
#     validate(item, POST_SCHEMA)

# [{'id': 1, 'title': 'Post 1'}, {'id': 2, 'title': 'Post 2'}, {'id': 3, 'title': 'Post 3'}]
