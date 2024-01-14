from django.contrib import admin

from memes.models import MemeTemplate, Meme


@admin.register(MemeTemplate)
class MemeTemplateAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_url', 'box_count', 'template_id', 'created_at']
    search_fields = ['name']
    readonly_fields = ['created_at']


@admin.register(Meme)
class MemeAdmin(admin.ModelAdmin):
    list_display = ['template', 'image_url', 'created_at']
    search_fields = ['template__name']
    readonly_fields = ['created_at']
