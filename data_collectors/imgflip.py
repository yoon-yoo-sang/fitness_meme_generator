import requests
import json

from config.settings import IMG_FLIP_USERNAME, IMG_FLIP_PASSWORD
from memes.models import MemeTemplate


class ImgFlipClient:
    def __init__(self):
        self.url = "https://api.imgflip.com"

    def get_top_memes(self):
        url = f"{self.url}/get_memes"
        response = requests.request("GET", url)
        memes = json.loads(response.text)['data']['memes']

        return memes

    def create_new_meme(self, meme_template: MemeTemplate, text_boxes: list[str]):
        template_id = meme_template.template_id
        url = f"{self.url}/caption_image"
        data = {
            "template_id": template_id,
            "username": IMG_FLIP_USERNAME,
            "password": IMG_FLIP_PASSWORD,
        }

        for i, text in enumerate(text_boxes):
            data[f"boxes[{i}][text]"] = text

        response = requests.post(url, data=data)

        return response.json()
