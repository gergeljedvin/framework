#!/usr/bin/env python
import requests
from framework.base.api_collection import APICollection

"""
    Test case 1: User not found - Sending not exist user id
    Test case 2: Bad request - Sending letters and special characters for user id (This test will fail)
"""


class TestUsersApi(object):

    def test_users_api_user_not_found(self):

        api_url = APICollection().reqres_free_api_users

        # Build the proper api url
        url = api_url + "/123456789"

        response = requests.request("GET", url)
        response_body = response.json()

        assert response.status_code == 404, "Status code is not 404, found : " + str(response.status_code) + str(response.text)
        assert response_body == {}

    def test_users_api_user_bad_request(self):

        api_url = APICollection().reqres_free_api_users

        # Build the proper api url
        url = api_url + "/A!B#C=D"

        response = requests.request("GET", url)

        # This api is not handling the bad request when letters and special characters were added, currently it is expected to fail
        assert response.status_code == 400, "Status code is not 400, found : " + str(response.status_code) + str(response.text)
