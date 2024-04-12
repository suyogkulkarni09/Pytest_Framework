import requests
import json
import random
import string
from Utilities.logger import CustLog

class PetStoreApiClient():
    '''def __init__(self, base_url):
        self.base_url = base_url'''
    with open('../Config/settings.json', 'r') as f:
        content = json.load(f)
    base_url = content["baseurl"]


    log = CustLog().log_details()


    def find_pets_by_status(self, status):
        # self.log.info("Sending Get Request")
        # self.log.info('Complete URL')
        completeURL = self.base_url + '/pet/findByStatus'
        # self.log.info(completeURL)
        print(completeURL)
        params = {'status': status}
        response = requests.get(completeURL, verify=False, params=params)
        # self.log.info("Response Code is")
        # self.log.info(response.status_code)
        # self.log.info("Response Body is")
        # self.log.info(response.text)
        return response

    def get_random_string(self, length):
        # choose from all lowercase letter
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        # print("Random string of length", length, "is:", result_str)
        return result_str

    def get_random_url(self):
        randomstring = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(12))
        randomurl = "https://" + randomstring + "/" + ''.join(
            random.choice(string.ascii_letters + string.digits) for x in range(4))
        return randomurl

    def add_new_pet(self):
        self.log.info("Sending Post Request")
        self.log.info('Complete URL')
        completeURL = self.base_url + '/pet'
        self.log.info(completeURL)
        jsonBody = {
            "id": random.randint(1, 9999999999),
            "category": {
                "id": random.randint(1, 999999),
                "name": self.get_random_string(6)
            },
            "name": self.get_random_string(8),
            "photoUrls": [
                self.get_random_url()
            ],
            "tags": [
                {
                    "id": random.randint(1, 9999),
                    "name": self.get_random_string(4)
                }
            ],
            "status": "available"
        }
        self.log.info(f"Request  body is set to = {jsonBody}")
        print(jsonBody)
        response = requests.post(completeURL, verify=False, json=jsonBody)
        self.log.info("Response Code is")
        self.log.info(response.status_code)
        self.log.info("Response Body is")
        self.log.info(response.text)
        return response
