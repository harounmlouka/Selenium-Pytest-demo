import requests

class BaseAPI:

    BASE_URL = ""

    def get(self, endpoint):
        return requests.get(self.BASE_URL + endpoint)

    def post(self, endpoint, json=None):
        return requests.post(self.BASE_URL + endpoint, json=json)

    def put(self, endpoint, json=None):
        return requests.put(self.BASE_URL + endpoint, json=json)

    def delete(self, endpoint):
        return requests.delete(self.BASE_URL + endpoint)