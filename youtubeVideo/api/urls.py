"""videos app URL Configuration"""

from django.urls import path
from api.views import get_videos

urlpatterns = [
    path('', get_videos)
]
