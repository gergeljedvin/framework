#!/usr/bin/env python
import json

import requests
from framework.base.api_collection import APICollection
from framework.base.user_credentials import UserCredentials


"""
    Test case: User is able to login successfully and the token value is not null in the response
"""


class TestLoginApi(object):

    def test_login_api_success_login(self):

        api_url = APICollection().reqres_free_api_login
        users_email = UserCredentials().users_email
        users_password = UserCredentials().users_password

        # POST request with proper credentials

        payload = json.dumps({
            "email": users_email,
            "password": users_password
        })

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", api_url, headers=headers, data=payload)
        response_body = response.json()

        assert response.status_code == 200, "Status code is not 200, found : " + str(response.status_code) + str(response.text)
        assert response_body['token'] is not None
