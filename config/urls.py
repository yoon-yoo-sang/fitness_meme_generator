from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from memes.views import MemeViewSet

router = routers.DefaultRouter()


router.register(r'memes', MemeViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path("admin/", admin.site.urls),
]


