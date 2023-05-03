#!/usr/bin/env python
import json
import requests
from framework.base.api_collection import APICollection

"""
    Test case: Create a user and update his name and job
"""


class TestUsersApi(object):

    def test_users_api_update_created_user(self):

        # Load the users api
        api_url = APICollection().reqres_free_api_users

        # Usually I use random string generator for these kind of data, but just to not overcomplicate now I will use these fixed once
        users_name = "Testuser"
        users_job = "Qa tester"

        # POST request to create a user

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
        # save the created user's id
        users_id = response_body['id']

        # Building the url with proper user id
        url = api_url + "/" + users_id
        users_name_edited = users_name + "Edited"
        users_job_edited = users_job + "Edited"

        # PUT request to update the created user

        payload = json.dumps({
            "name": users_name_edited,
            "job": users_job_edited
        })

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("PUT", url, headers=headers, data=payload)
        response_body = response.json()

        assert response.status_code == 200, "Status code is not 200, found : " + str(response.status_code) + str(response.text)
        assert response_body['name'] == users_name_edited
        assert response_body['job'] == users_job_edited
