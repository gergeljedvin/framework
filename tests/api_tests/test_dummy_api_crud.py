#!/usr/bin/env python
from framework.base.config import env_config
from framework.base.get_token import Token
import requests
from barnum import gen_data


class DummyApiCRUD(object):

    def test_get_all_objects(self):

        api_url = "https://api.restful-api.dev/objects/"

        # POST request - Create an object
        url = api_url
        dummy_name = "QA-TEST"

        payload = {"name": dummy_name}

        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        response = requests.request("POST", url, params=payload, headers=headers)
        assert response.status_code == 201, "Status code is not 201, found : " + str(response.status_code) + str(response.text)

        response_body = response.json()
        assert response_body['name'] == dummy_name
        object_id = response.body['id']

        # GET Request - Get the created object
        url = api_url + object_id

        response = requests.request("GET", url, params=payload, headers=headers)
        assert response.status_code == 200, "Status code is not 200, found : " + str(response.status_code) + str(response.text)

        response_body = response.json()
        assert response_body['id'] == object_id
        assert response_body['name'] == dummy_name

        # PUT request - Update the created object
        url = api_url + object_id
        dummy_new_name = "QA-TEST-EDITED"

        payload = {"name": dummy_new_name}

        response = requests.request("PUT", url, params=payload, headers=headers)
        assert response.status_code == 200, "Status code is not 200, found : " + str(response.status_code) + str(response.text)

        url = api_url + object_id

        response = requests.request("GET", url, params=payload, headers=headers)
        assert response.status_code == 200, "Status code is not 200, found : " + str(response.status_code) + str(response.text)

        response_body = response.json()
        assert response_body['name'] == dummy_new_name

        # DELETE Request - Delete the created object
        url = api_url + object_id

        response = requests.request("DELETE", url, params=payload, headers=headers)
        assert response.status_code == 204, "Status code is not 204, found : " + str(response.status_code) + str(response.text)
