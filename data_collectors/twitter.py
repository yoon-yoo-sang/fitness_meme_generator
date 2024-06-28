import os
import tweepy
import requests


class TwitterClient:
    def __init__(self):
        self.bearer_token = os.environ.get("TWITTER_BEARER_TOKEN")
        consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
        consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")
        access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
        access_token_secret = os.environ.get("TWITTER_ACCESS_SECRET_TOKEN")

        self.old_api = tweepy.API(
            tweepy.OAuthHandler(consumer_key, consumer_secret, access_token, access_token_secret)
        )
        self.client = tweepy.Client(self.bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)

    def get_user_list(self, user_name):
        url = f"https://api.twitter.com/2/users/by/username/{user_name}"
        headers = {"Authorization": f"Bearer {self.bearer_token}"}
        response = requests.get(url, headers=headers)
        return response.json()

    def get_token(self):
        token_url = "https://api.twitter.com/oauth2/token"
        token_headers = {"Authorization": f"Basic {self.bearer_token}"}
        token_data = {"grant_type": "client_credentials"}
        response = requests.post(token_url, headers=token_headers, data=token_data)
        return response.json()

    def post_tweet(self, text):
        try:
            self.client.create_tweet(text=text)
            return "Tweet posted successfully"
        except Exception as e:
            raise e

    def post_image(self, image):
        try:
            media1 = self.old_api.media_upload(filename="image.jpg", file=image)
            self.client.create_tweet(media_ids=[media1.media_id])
            return "Image posted successfully"
        except Exception as e:
            raise e
