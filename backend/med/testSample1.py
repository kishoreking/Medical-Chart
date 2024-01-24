
from django.test import TestCase

import pytest,json,requests

class NewTestCase(TestCase):
    token=""
    def setUp(self):
        # Set up the token for each test method
        self.token = self.testApiToken()

    def testApiToken(self):
        # global token
        url = 'http://localhost:8000/api/token/'
        payload = {
                        "username": "9136120050",
                        "password": "Msg@1503!"
                    }
        print(payload)
        response = requests.post(url, data=payload)
        print(response.text)
        token = response.json().get("access")
        print(self.token)
        # assert response.status_code == 200
        return token

    def testVendorType(self):
        url = 'http://localhost:8000/toweross/SiteInfoGetApi/'
        payload = {
                    "ownername": "DEPL",
                    "VendorType": "",
                    # "VendorCompany": {"all": {"min": 0,"max": 10}}
                    }
        print("/////",self.token)
        headers = {
        'Authorization': f'Bearer {self.token}',
        'Content-Type': 'application/json',
        }
        response = requests.post(url, json=payload,headers=headers)
        assert response.status_code == 200  

    def testVendorCompany(self):
        url = 'http://localhost:8000/toweross/SiteInfoGetApi/'
        payload = {
                    "ownername": "DEPL",
                    "VendorCompany": {"all": {"min": 0,"max": 10}}
                    }
        # print(payload)
        headers = {
        'Authorization': f'Bearer {self.token}',
        'Content-Type': 'application/json',
        }
        response = requests.post(url, json=payload,headers=headers)
        # print(response)
        assert response.status_code == 200       

    def testToweruserRoles(self):
        url = 'http://localhost:8000/toweross/Touweuserroles/'
        payload = {
                "min": 0,
                "max": 100,
                "filter": "Group",
                "ownername": "SMRT",
                "National": "INDIA",
                "Region": "",
                "cluster": "",
                "State": "",
                "MaintenancePoint": "",
                "area": "",
                "objectname": "",
                "startdate":"2024-01-01",
                "enddate":"2024-01-09" ,
                "userList":[255,3]
            }
        # print(payload)
        headers = {
        'Authorization': f'Bearer {self.token}',
        'Content-Type': 'application/json',
        }
        response = requests.post(url, json=payload,headers=headers)
        # print(response.text)
        assert response.status_code == 200          