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
        api_keys = settings.GOOGLE_API_KEYS
        time_now = datetime.now()
        last_updated_time=time_now - timedelta(minutes=5)

        valid= False

        for api_key in api_keys:
            try:
                youtube = build('youtube', 'v3', developerKey=api_key)
                request = youtube.search().list(
                    q='football',
                    part='snippet',
                    maxResults=50,
                    order='date',
                    publishedAfter=last_updated_time.replace(microsecond=0).isoformat()+'Z',
                )
                response = request.execute()
                valid = True

                
                # if(len(response['items'])>0):
                #     break

            except HttpError as e:
                code=e.resp.status
                if not(code==403 or code==400):
                    break
            if valid:
                break

        print(valid)
        if valid:
            for item in response['items']:
                print("response",item)
                video_id = item['id']['videoId']
                title = item['snippet']['title']
                description = item['snippet']['description']
                thumbnail_urls = item['snippet']['thumbnails']['default']['url']
                published_at = item['snippet']['publishedAt']
                channel_id = item['snippet']['channelId']
                channel_title = item['snippet']['channelTitle']
                YoutubeVideos.objects.create(
                    video_id=video_id,
                    title=title,
                    description=description,
                    thumbnail_urls=thumbnail_urls,
                    published_at=published_at,
                    channel_id=channel_id,
                    channel_title=channel_title
                )