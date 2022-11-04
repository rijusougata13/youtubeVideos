import asyncio
import os
from apiKeys.models import ApiKey
from django.core.management import call_command
from django.core.management.commands.runserver import Command as BaseCommand
import environ
from youtubeVideo import settings

loop = asyncio.get_event_loop()


def start_sync():
    print("Starting Sync with Youtube...")
    call_command('syncYoutube')


class Command(BaseCommand):

    def handle(self, *args, **options):
        API_KEYS=settings.GOOGLE_API_KEYS
        for key in API_KEYS:
            
            ApiKey.objects.create(key=key,name=key)

        if os.environ.get('RUN_MAIN') != 'true':
            loop.run_in_executor(None, start_sync)
        super(Command, self).handle(*args, **options)
