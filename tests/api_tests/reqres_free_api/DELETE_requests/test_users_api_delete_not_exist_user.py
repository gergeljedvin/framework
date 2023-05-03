#!/usr/bin/env python
import requests
from framework.base.api_collection import APICollection

"""
    Test case: Try to delete a not existing user
        NOTE: This test will fail because this free api will always return 204, but in this case usually api should return 404 Not Found
              So I assert for that status code
"""


class TestUsersApi(object):

    def test_users_api_delete_not_exist_user(self):

        # Load the users api
        api_url = APICollection().reqres_free_api_users

        # DELETE request, building the url with not existing user id
        url = api_url + "/A1B2C3"

        response = requests.request("DELETE", url)

        # Try to assert for proper status code, 404 for resource not exist / not found
        assert response.status_code == 404, "Status code is not 404, found : " + str(response.status_code) + str(response.text)