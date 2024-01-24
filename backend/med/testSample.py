
from django.test import Client, TestCase

import pytest,json,requests

# def func(x):
#     return x + 2
# def test_answer():
#     assert func(3) == 5

class YourTestCase(TestCase):

    def testMedicalChartStatusReset(self):

        url = 'http://127.0.0.1:8080/medtask/medicalChartStatusReset/'
        response = requests.post(url)
        assert response.status_code == 200
        assert response.text == '"Success"' 

    def testFirstTimeAssingment(self):

        url = 'http://127.0.0.1:8080/medtask/firstTimeAssingment/'
        response = requests.post(url)
        assert response.status_code == 200
        assert response.text == '"Success"' 

    def testMedicalCharAllocatedUserInfoGetApi(self):

        url = 'http://127.0.0.1:8080/medtask/medicalCharAllocatedUserInfoGetApi/'
        response = requests.get(url)
        assert response.status_code == 200      

    def testMedicalChartInfoGetApi(self):

        url = 'http://127.0.0.1:8080/medtask/medicalChartInfoGetApi/'
        response = requests.get(url)
        assert response.status_code == 200 

    def testmedicalChartChangeStatus(self):

        url = 'http://127.0.0.1:8080/medtask/medicalChartChangeStatus/'
        payload = {"id":1,"status":3}
        print(payload)
        response = requests.get(url, data=payload)
        assert response.status_code == 200
        assert response.text == '"Success"'               

