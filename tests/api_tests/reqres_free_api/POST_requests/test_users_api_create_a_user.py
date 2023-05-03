#!/usr/bin/env python
import json
import requests
from framework.base.api_collection import APICollection

"""
    Test case: User is able to login successfully and the token is not null in the response
"""


class TestUsersApi(object):

    def test_users_api_create_a_user(self):

        api_url = APICollection().reqres_free_api_users
        users_name = "Testuser"
        users_job = "Qa tester"

        payload = json.dumps({
            "name": users_name,
            "job": users_job
        })

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", api_url, headers=headers, data=payload)
        response_body = response.json()

        assert response.status_code == 200 or 201, "Status code is not 200 or 201, found : " + str(response.status_code) + str(response.text)
        assert response_body['name'] == users_name
        assert response_body['job'] == users_job
        assert response_body['id'] is not None
