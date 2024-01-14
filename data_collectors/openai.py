import json
import requests

from config.settings import OPENAI_API_KEY


class OpenAIClient:
    def __init__(self):
        self.api_key = OPENAI_API_KEY
        self.url = "https://api.openai.com/v1/chat/completions"

    def create_meme(self, meme_name: str, box_count: int, recent_trend: str):
        instruction = f"""
            recent trend: {recent_trend}
            meme name: {meme_name}
            box count: {box_count}
            response format (json)
            ```
                box1: $text
                box2: $text
                ...
            ```
            Make funny memes about fitness
        """

        headers = {
            'Content-Type': 'application/json',
            "Authorization": f"Bearer {self.api_key}",
        }

        data = {
            "model": "gpt-4-1106-preview",
            "messages": [{"role": "user", "content": instruction}],
            "response_format": {"type": "json_object"},
            "temperature": 0.7
        }

        response = requests.request("POST", self.url, headers=headers, data=json.dumps(data))
        return json.loads(response.text)['choices'][0]['message']['content']
