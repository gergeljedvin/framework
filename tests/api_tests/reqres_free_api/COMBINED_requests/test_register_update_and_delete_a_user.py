#!/usr/bin/env python
import json
import requests
from framework.base.api_collection import APICollection
from framework.base.user_credentials import UserCredentials

"""
    Test case: Register a user, update his name and job, delete the created user, check that the user not exist anymore
    
    NOTE: With this free api only specific users are able to success the register, they cannot be deleted, so it is 
          expected from this test to fail. The logic behind this is to combine multiple api calls with different 
          endpoints
"""


class TestUsersApi(object):

    def test_register_update_and_deleted_a_user(self):

        # Load the api endpoints
        register_api_url = APICollection().reqres_free_api_register
        users_api_url = APICollection().reqres_free_api_users

        # Usually random generated emails and passwords should be used here, I have used these because the free api
        # only support predefined user credentials for registration

        users_email = UserCredentials().users_email
        users_password = UserCredentials().users_password

        # POST request to register a user

        payload = json.dumps({
            "email": users_email,
            "password": users_password
        })

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", register_api_url, headers=headers, data=payload)
        response_body = response.json()

        # Assert that the registration was successful and that the token is not empty
        assert response.status_code == 200, "Status code is not 200, found : " + str(response.status_code) + str(response.text)
        assert response_body['token'] is not None
        # Save the registered user id for the next request
        users_id = str(response_body['id'])

        # Build the correct users url for other requests with the specific id
        url = users_api_url + "/" + users_id

        # PUT request to update the registered user's name and job

        users_name = "Qa Tester"
        users_job = "Tester"

        payload = json.dumps({
            "name": users_name,
            "job": users_job
        })

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("PUT", url, headers=headers, data=payload)
        response_body = response.json()

        assert response.status_code == 200, "Status code is not 200, found : " + str(response.status_code) + str(response.text)
        assert response_body['name'] == users_name
        assert response_body['job'] == users_job

        # GET request to check that it will return the proper user with correct email, name and job

        response = requests.request("GET", url)
        response_body = response.json()

        assert response.status_code == 200, "Status code is not 200, found : " + str(response.status_code) + str(response.text)
        assert response_body['data']['name'] == users_email
        assert response_body['data']['name'] == users_name
        assert response_body['data']['job'] == users_job

        # DELETE request to delete the registered user

        response = requests.request("DELETE", url)
        assert response.status_code == 204, "Status code is not 204, found : " + str(response.status_code) + str(response.text)

        # GET request to search again for the deleted user to assert that he is deleted and that the response will return that the user not exist

        response = requests.request("GET", url)
        assert response.status_code == 404, "Status code is not 404, found : " + str(response.status_code) + str(response.text)
