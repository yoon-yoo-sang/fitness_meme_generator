import json
import requests

from config.settings import OPENAI_API_KEY


class OpenAIClient:
    def __init__(self):
        self.api_key = OPENAI_API_KEY
        self.url = "https://api.openai.com/v1/chat/completions"

    def send(self, instruction):
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

    def search_trends(self, count: int = 3):
        instruction = f"""
            can you tell me {count} recent fitness meme{'' if count == 1 else 's'} or issues or controvercials in america?
            response format (json)
            ```
                recent_issues: [$text...]
            ```
        """

        return json.loads(self.send(instruction))['recent_issues']

    def create_meme(self, meme_name: str, box_count: int, recent_trend: str):
        instruction = f"""
            recent trend: {recent_trend}
            meme name: {meme_name}
            box count: {box_count}
            response format (json)
            ```
                boxes: [$caption1, $caption2, ...]
            ```
            Make funny memes about fitness
        """

        boxes = json.loads(self.send(instruction))['boxes']

        preprocessed_boxes = []

        for box in boxes:
            preprocessed_box = box
            if ':' in box:
                preprocessed_box = box.split(':')[1].strip()
            preprocessed_boxes.append(preprocessed_box)

        return preprocessed_boxes
