from rest_framework import serializers

from .models import Meme, MemeTextBox


class MemeSerializer(serializers.ModelSerializer):
    text_boxes = serializers.StringRelatedField(many=True)

    class Meta:
        model = Meme
        fields = ['id', 'template', 'text_boxes', 'image_url', 'created_at']

    def create(self, validated_data):
        text_boxes = validated_data.pop('text_boxes')
        meme = Meme.objects.create(**validated_data)
        for text_box in text_boxes:
            meme.text_boxes.create(**text_box)
        return meme

    def update(self, instance, validated_data):
        text_boxes = validated_data.pop('text_boxes')
        instance.template = validated_data.get('template', instance.template)
        instance.save()
        keep_text_boxes = []
        for text_box in text_boxes:
            if "id" in text_box.keys():
                if MemeTextBox.objects.filter(id=text_box["id"]).exists():
                    c = MemeTextBox.objects.get(id=text_box["id"])
                    c.text = text_box.get('text', c.text)
                    c.box_number = text_box.get('box_number', c.box_number)
                    c.save()
                    keep_text_boxes.append(c.id)
                else:
                    continue
            else:
                c = MemeTextBox.objects.create(**text_box, meme=instance)
                keep_text_boxes.append(c.id)
        for text_box in instance.text_boxes.all():
            if text_box.id not in keep_text_boxes:
                text_box.delete()
        return instance
