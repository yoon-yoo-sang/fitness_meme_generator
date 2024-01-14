import requests

from config.settings import TWITTER_TOKEN


class TwitterClient:
    def __init__(self):
        self.bearer_token = TWITTER_TOKEN

    def get_user_list(self, user_name):
        url = f"https://api.twitter.com/2/users/by/username/{user_name}"
        headers = {"Authorization": f"Bearer {self.bearer_token}"}
        response = requests.request("GET", url, headers=headers)
        return response.text
