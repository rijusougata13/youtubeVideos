from django.shortcuts import render
import getopt, sys
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.core.paginator import Paginator, EmptyPage
from django.forms import model_to_dict
from django.http import JsonResponse
from .models import *
from .serializers import *
from api.models import Video

from rest_framework import generics
from rest_framework.pagination import CursorPagination




class ResultsPagination(CursorPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100

# Searching is implemented using DRF Filters
# DRF filter by default uses [icontains] and thus the search by default supports partial searches

class YoutubeItems(generics.ListAPIView):
    search_fields = ['title', 'description']
    filter_backends = (filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter)
    filterset_fields = ['yt_id','title']
    ordering = ('-published_at')
    queryset = Video.objects.all()
    serializer_class = VideosSerializer
    pagination_class = ResultsPagination


def get_videos(request):
    """View for API to get videos in descending order of publish date-time
    Supports Pagination
    :param (URL param) page = int page_number (default 1)
    :returns JSON Response with data or error
    """

    # Allow only GET request
    if request.method != 'GET':
        return JsonResponse({"details": "Method not allowed"}, status=405)

    # Get all video objects sorted by reverse publish date-time
    videos = Video.objects.all().order_by('-published_at')

    # Create paginator
    paginator = Paginator(videos, 50)

    # Get Page number from URL params (default 1)
    page_no = int(request.GET.get('page') or '1')

    # Try to get requested page number from paginator.
    # If it doesn't exist return 404 with proper details
    try:
        page = paginator.page(page_no)
    except EmptyPage:
        return JsonResponse({"details": "Page out of range"}, status=404)

    # Get next and previous page number if exists, else None
    next_page = page.next_page_number() \
        if page.has_next() else None
    prev_page = page.previous_page_number() \
        if page.has_previous() else None

    # Get list of dicts of video from the page
    paginated_videos = [model_to_dict(v) for v in list(page)]

    # Return the JSON Response
    return JsonResponse({
        "next_page": next_page,
        "previous_page": prev_page,
        "videos": paginated_videos
    })
