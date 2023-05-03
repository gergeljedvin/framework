#!/usr/bin/env python
import requests
import json

class TestDummyApiCRUD(object):

    def test_api_crud(self):

        # Free api
        api_url = "http://api.restful-api.dev/objects"

        # POST request - Create an object
        url = api_url
        dummy_name = "QA-TEST"

        payload = json.dumps({
            "name": dummy_name,
            "data": {
                "color": "Cloudy White",
                "capacity": "128 GB"
            }
        })

        headers = {
            'Content-Type': 'application/json',
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        assert response.status_code == 200 or 201, "Status code is not 200 or 201, found : " + str(response.status_code) + str(response.text)

        response_body = json.loads(response.text)
        assert response_body['name'] == "QA-TEST"

        # GET Request - Get an item with id "1"
        url = api_url + "/1"

        response = requests.request("GET", url, data=payload, headers=headers)
        assert response.status_code == 200, "Status code is not 200, found : " + str(response.status_code) + str(response.text)

        response_body = response.json()
        assert response_body['id'] == "1"
