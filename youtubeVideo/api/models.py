from django.db import models

# Model for storing the video details

class YoutubeVideos(models.Model):
    video_id = models.CharField(null=False,blank=False, max_length=100)
    title = models.CharField(null=True,blank=True,max_length=100)
    description = models.CharField(null=True,blank=True,max_length=100)
    thumbnail_urls = models.URLField()
    published_at = models.DateTimeField()
    channel_id = models.CharField(null=False,blank=False,max_length=100)
    channel_title = models.CharField(null=True,blank=True,max_length=100)
    created = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
    )

