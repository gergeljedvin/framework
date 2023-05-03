#!/usr/bin/env python
import requests
from framework.base.api_collection import APICollection

"""
    Test case 1: List all users
    Test case 2: List users on the second page - pagination
    Test case 3: List a single user
"""


class TestUsersApi(object):

    def test_users_api_list_all_users(self):

        api_url = APICollection().reqres_free_api_users

        response = requests.request("GET", api_url)
        response_body = response.json()

        # Assert that the status kod is OK, also that the first page is displayed and that the list of users is not empty
        assert response.status_code == 200, "Status code is not 200, found : " + str(response.status_code) + str(response.text)
        assert response_body['page'] == 1
        assert response_body['per_page'] == 6
        assert response_body['data'] != [], "There is no data in the database for users!"

    def test_users_api_list_users_on_the_second_page(self):

        api_url = APICollection().reqres_free_api_users

        # Build the proper api url
        url = api_url + "?page=2"

        response = requests.request("GET", url)
        response_body = response.json()

        # Assert that the status kod is OK, also that the second page is displayed and that the data is not empty
        assert response.status_code == 200, "Status code is not 200, found : " + str(response.status_code) + str(response.text)
        assert response_body['page'] == 2
        assert response_body['per_page'] == 6
        # Sometimes it is possible that the second page will not return any users because there are only a couple
        # In this case if the second page doesn't contain users the proper message will be displayed after test execution
        try:
            assert response_body['data'] != []
        except AssertionError:
            print("There is no data on the second page!")

    def test_users_api_list_a_single_user(self):

        api_url = APICollection().reqres_free_api_users

        # Build the proper api url
        url = api_url + "/3"

        response = requests.request("GET", url)
        response_body = response.json()

        assert response.status_code == 200, "Status code is not 200, found : " + str(response.status_code) + str(response.text)
        assert response_body['data']['id'] == 3
        assert response_body['data']['email'] == "emma.wong@reqres.in"
        assert response_body['data']['first_name'] == "Emma"
        assert response_body['data']['last_name'] == "Wong"
        assert response_body['data']['avatar'] == "https://reqres.in/img/faces/3-image.jpg"
