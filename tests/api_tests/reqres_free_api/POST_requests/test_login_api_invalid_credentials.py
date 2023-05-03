#!/usr/bin/env python
import json

import requests
from framework.base.api_collection import APICollection
from framework.base.user_credentials import UserCredentials


"""
    Test case 1: User is not able to login because the added email is not in correct format
    Test case 2: User is not able to login because the added password is incorrect
    Test case 3: User is not able to login because wrong credentials were added
"""


class TestLoginApi(object):

    # Test case 1
    def test_login_api_invalid_email_format(self):

        api_url = APICollection().reqres_free_api_login
        users_password = UserCredentials().users_password

        # The added email is not in correct format
        payload = json.dumps({
            "email": "test@",
            "password": users_password
        })

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", api_url, headers=headers, data=payload)
        response_body = response.json()

        assert response.status_code == 400, "Status code is not 400, found : " + str(response.status_code) + str(response.text)
        assert response_body['error'] == "user not found"

    # Test case 2
    def test_login_api_wrong_password_added(self):

        api_url = APICollection().reqres_free_api_login
        users_email = UserCredentials().users_email

        # The added password is incorrect
        payload = json.dumps({
            "email": users_email,
            "password": "123"
        })

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", api_url, headers=headers, data=payload)
        response_body = response.json()

        """
        NOTE: This test will fail because the user can log in with any password!
        """
        assert response.status_code == 400, "Status code is not 400, found : " + str(response.status_code) + str(response.text)
        assert response_body['error'] == "Incorrect username or password"

    # Test case 3
    def test_login_api_not_existing_user(self):

        api_url = APICollection().reqres_free_api_login

        # Not existing user is added in payload
        payload = json.dumps({
            "email": "test@test.com",
            "password": "123"
        })

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", api_url, headers=headers, data=payload)
        response_body = response.json()

        assert response.status_code == 400, "Status code is not 400, found : " + str(response.status_code) + str(response.text)
        assert response_body['error'] == "user not found"
