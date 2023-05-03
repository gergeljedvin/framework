#!/usr/bin/env python
import json

import requests
from framework.base.api_collection import APICollection
from framework.base.user_credentials import UserCredentials


"""
    Test case 1: Try to login with missing credentials
    Test case 2: Try to log in with only password added
    Test case 3: Try to log in with only email added
"""


class TestLoginApi(object):

    # Test case 1
    def test_login_api_missing_credentials(self):

        api_url = APICollection().reqres_free_api_login

        payload = json.dumps({
            "email": "",
            "password": ""
        })

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", api_url, headers=headers, data=payload)
        response_body = response.json()

        assert response.status_code == 400, "Status code is not 400, found : " + str(response.status_code) + str(response.text)
        assert response_body['error'] == "Missing email or username"

    # Test case 2
    def test_login_api_only_password_added(self):

        api_url = APICollection().reqres_free_api_login
        users_password = UserCredentials().users_password

        # Missing email in payload
        payload = json.dumps({
            "email": "",
            "password": users_password
        })

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", api_url, headers=headers, data=payload)
        response_body = response.json()

        assert response.status_code == 400, "Status code is not 400, found : " + str(response.status_code) + str(response.text)
        assert response_body['error'] == "Missing email or username"

    # Test case 3
    def test_login_api_email_added_password_is_missing(self):

        api_url = APICollection().reqres_free_api_login
        users_email = UserCredentials().users_email

        # Missing password in payload
        payload = json.dumps({
            "email": users_email,
            "password": ""
        })

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", api_url, headers=headers, data=payload)
        response_body = response.json()

        assert response.status_code == 400, "Status code is not 400, found : " + str(response.status_code) + str(response.text)
        assert response_body['error'] == "Missing password"
