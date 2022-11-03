from rest_framework import serializers
from .models import *

class VideosSerializer(serializers.ModelSerializer):

    class Meta:
        model = YoutubeVideos
        fields = "__all__"
