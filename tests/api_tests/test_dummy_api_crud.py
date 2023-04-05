#!/usr/bin/env python
import requests


class TestDummyApiCRUD(object):

    def test_api_crud(self):

        # Free api
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
        assert response.status_code == 200, "Status code is not 200, found : " + "" + str(response.status_code) + str(response.text)

        # GET Request - Get an item with id "1"
        url = api_url + "1"

        response = requests.request("GET", url, params=payload, headers=headers)
        assert response.status_code == 200, "Status code is not 200, found : " + str(response.status_code) + str(response.text)

        response_body = response.json()
        assert response_body['id'] == "1"
