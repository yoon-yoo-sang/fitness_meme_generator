import io

import boto3
import requests
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from config.settings import AWS_ACCESS_KEY, AWS_SECRET_KEY
from data_collectors.imgflip import ImgFlipClient
from data_collectors.openai import OpenAIClient
from .models import Meme, MemeTemplate, MemeTextBox
from .serializers import MemeSerializer


class MemeViewSet(viewsets.ModelViewSet):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer

    @action(detail=False, methods=['post'])
    def generate(self, request):
        meme_template = MemeTemplate.objects.get(pk=request.data['meme_template_id'])
        recent_trend = request.data.get('recent_trend', '')
        meme_data = self.generate_meme(meme_template, recent_trend)
        return Response(meme_data)

    @staticmethod
    def generate_meme(meme_template: MemeTemplate, recent_trend: str = ''):
        openai_client = OpenAIClient()
        img_flip_client = ImgFlipClient()

        if not recent_trend:
            recent_trend = openai_client.search_trends(1)[0]

        boxes: list = openai_client.create_meme(meme_template.name, meme_template.box_count, recent_trend)

        meme_image_url = img_flip_client.create_new_meme(meme_template, boxes)['data']['url']

        meme = Meme.objects.create(template=meme_template, image_url=meme_image_url)
        for i, box in enumerate(boxes):
            MemeTextBox.objects.create(meme=meme, text=box, box_number=i)

        image_file = requests.get(meme_image_url).content

        s3_client = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
            region_name='ap-northeast-2',
        )
        s3_client.upload_fileobj(io.BytesIO(image_file), 'fitness-memes', f"{recent_trend}_{meme_template.name}.jpg")

        serializer = MemeSerializer(meme)

        return serializer.data
