import os
from django_cron import CronJobBase, Schedule

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from .models import YoutubeVideos
from youtubeVideo import settings
from datetime import datetime, timedelta

class YoutubeCron(CronJobBase):
    
    INTERVAL_MINS = 1

    schedule = Schedule(run_every_mins=INTERVAL_MINS)
    code='youtubeVideo.api.cron.YoutubeCron'

    def do(self):
        print("Cron Job started")
        api_keys = settings.GOOGLE_API_KEYS
        time_now = datetime.now()
        last_updated_time=time_now - timedelta(minutes=self.INTERVAL_MINS)
