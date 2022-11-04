import datetime
import os
import sys
from time import sleep
from youtubeVideo import settings
from api.models import Video
from apiKeys.models import ApiKey
from django.core.management.base import BaseCommand

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


Interval=10

def youtube_search(api_key, query, max_results, published_after, page_token=None):
    youtube = build('youtube', 'v3',
                    developerKey=api_key)
    try:
        search_response = youtube.search().list(
            q=query,
            type='video',
            order='date',
            part='id,snippet',
            publishedAfter=published_after,
            pageToken=page_token,
            maxResults=max_results
        ).execute()
        return search_response
    except HttpError as e:
        raise e


def save_new_videos(new_videos):
    saved_count = 0
    for video in new_videos['items']:
        video_check = Video.objects.filter(yt_id=video['id']['videoId'])
        if video_check.exists():
            continue

        Video.objects.create(
            yt_id=video['id']['videoId'],
            published_at=video['snippet']['publishedAt'],
            title=video['snippet']['title'],
            description=video['snippet']['description'],
            thumbnail_url=video['snippet']['thumbnails']['medium']['url']
        )
        saved_count += 1
    return saved_count


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Sync Service Started...')
        sys.stdout.flush()

        
        api_keys = ApiKey.objects.all()
        current_api_key = api_keys.first().key if api_keys.exists() else 'random'
        current_api_key_num = 0

        while True:
            videos = Video.objects.all().order_by('-published_at')
            if videos.exists():
                published_after = videos.first().published_at.replace(
                    tzinfo=None)
            else:
                published_after = datetime.datetime.utcnow() - \
                                  datetime.timedelta(minutes=30)

            next_page = None
            published_after_str = published_after.isoformat("T") + "Z"
            saved_count = 0

            while True:
                # Get new videos
                try:
                    new_videos = youtube_search(current_api_key,
                                                'football',
                                                50,
                                                published_after_str,
                                                next_page)
                    num_videos = len(new_videos['items'])
                    if num_videos > 0:
                        cnt = 0
                        for video in new_videos['items']:
                            video_check = Video.objects.filter(yt_id=video['id']['videoId'])
                            if video_check.exists():
                                continue

                            Video.objects.create(
                                yt_id=video['id']['videoId'],
                                published_at=video['snippet']['publishedAt'],
                                title=video['snippet']['title'],
                                description=video['snippet']['description'],
                                thumbnail_url=video['snippet']['thumbnails']['medium']['url']
                            )
                            cnt += 1


                        saved_count += cnt
                   
                    if 'nextPageToken' in new_videos and num_videos > 0:
                        next_page = new_videos['nextPageToken']
                    else:
                        break
                    msg = "Sync service: Added {} new videos at {}"
                    self.stdout.write(msg.format(
                        saved_count,
                        datetime.datetime.utcnow()
                    ))

                except HttpError as e:
                    api_keys = ApiKey.objects.all()
                    if not api_keys.exists():
                        self.stdout.write(
                            "No API Keys present in database, please add some")
                        break
                    if e.resp['status'] == '403':
                        self.stdout.write("Sync service: API Key error, using next key")
                        current_api_key_num = (current_api_key_num+1) % api_keys.count()
                        current_api_key = api_keys[current_api_key_num].key
                        if current_api_key_num == api_keys.count() - 1:
                            break
                        else:
                            continue
                    else:
                        self.stderr.write("Sync service: Error calling API")
                        self.stderr.write(e)
                finally:
                    sys.stdout.flush()
                    sleep(Interval)
