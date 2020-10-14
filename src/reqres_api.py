import requests
import json


class ReqresApi:
    @staticmethod
    def resources(link):
        response = requests.get(link)
        result = response.json()

        text = json.dumps(result, indent=4)
        return text
