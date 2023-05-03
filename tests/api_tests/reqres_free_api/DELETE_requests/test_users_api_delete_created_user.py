#!/usr/bin/env python
import json
import requests
from framework.base.api_collection import APICollection

"""
    Test case: Create a user and try to delete it
"""


class TestUsersApi(object):

    def test_users_api_delete_created_user(self):

        # POST request to create a user first
        api_url = APICollection().reqres_free_api_users

        users_name = "Testuser123"
        users_job = "Qa tester 123"

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
        # Save the created user's id
        users_id = response_body['id']

        # DELETE request to delete the created user
        url = api_url + "/" + users_id

        response = requests.request("DELETE", url, headers=headers, data=payload)

        # In this test I can only test the status of 204 code because the response is empty
        # Usually it should return that the content or user was successfully deleted
        assert response.status_code == 204, "Status code is not 204, found : " + str(response.status_code) + str(response.text)
