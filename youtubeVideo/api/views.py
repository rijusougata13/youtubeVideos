from django.shortcuts import render
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .serializers import *

from rest_framework import generics
from rest_framework.pagination import CursorPagination

# Searching with DRF and DjangoFilterBackend

class VideosPagination(CursorPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100  


class VideosList(generics.ListAPIView):
    queryset = YoutubeVideos.objects.all()
    serializer_class = VideosSerializer
    pagination_class = VideosPagination
   
