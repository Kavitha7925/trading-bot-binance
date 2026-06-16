import requests

class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self, endpoint: str):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)
        return response.json()

    def post(self, endpoint: str, data: dict):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=data)
        return response.json()