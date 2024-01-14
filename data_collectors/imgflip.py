import requests
import json


class ImgFilpClient:
    def __init__(self):
        self.url = "https://api.imgflip.com"

    def get_top_memes(self):
        url = f"{self.url}/get_memes"
        response = requests.request("GET", url)
        memes = json.loads(response.text)['data']['memes']

        return memes
