import pytest
import sys
import random
import requests
from requests.auth import HTTPBasicAuth

#Testcase 1 : Verify Fetching all the alert profiles with status code and content
def test_getAlertProfiles_GET():
    global endPointUrl
    endPointUrl = 'https:xxxxxxxx'
    global headerList
    headerList = {
        "Accept":"application/json",
        "Authorization":"Token xxxx"
    }

    global email
    email = 'testuser'
    global password
    password = '46tttt77'
    response = requests.get(endPointUrl, headers=headerList, auth = HTTPBasicAuth(email , password))
    print(response.status_code)
    assert response.status_code == 200
    #print(response.body)

    """
    assert response.headers['Content-Type'] == "application/json"
    response_body = response.json()
    assert response_body["orgId"] == "89898989"
    """

#Testcase 2 : Verify creating a new alert Profile
def test_createNewAlertProfile_POST():
    response = requests.post(endPointUrl, headers=headerList, auth = HTTPBasicAuth(email , password), data={
            "id":null,
            "name":"test",
            "useAsDefault":false,
            "visible":true,
            "orgId":89898989,
            "categoryType":"WebPath",
            "subCategoryType":"Browser",
            "attribs":[
            {
                "id":null,
                "param":"Connectivity",
                "scope":"Overall",
                "overInterval":2,
                "underInterval":2,
                "value":0
            }
                        ],
            "global":false
        })
    print(response.status_code)
    assert response.status_code == 200
    #print(response.body)
