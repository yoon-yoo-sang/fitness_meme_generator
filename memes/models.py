from django.db import models


class MemeTemplate(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image_url = models.URLField()
    box_count = models.IntegerField()
    template_id = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Meme(models.Model):
    template = models.ForeignKey(MemeTemplate, on_delete=models.CASCADE)
    image_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Meme from {self.template.name}"


class MemeTextBox(models.Model):
    meme = models.ForeignKey(Meme, related_name='text_boxes', on_delete=models.CASCADE)
    text = models.TextField()
    box_number = models.IntegerField()

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['box_number']
