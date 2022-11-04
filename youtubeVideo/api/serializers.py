from rest_framework import serializers
from .models import *

class VideosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = "__all__"