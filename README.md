# youtubeVideos

**API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.**


# Tech stack
- Django Framework (DRF)
- sqlite 
- python


# Feature
- Support Django-admin panel 
- Pagination supported
- Filter, Optimize search support
- Specific dashboard for all the features at /api
- Handle Multiple api key if any of them expired
- easily run with docker
- optimized codebase

# Run Locally:

* ## Using Docker - 
   **Make sure you have docker and docker-compose installed. If not, refer: https://docs.docker.com/install/**
   - Put env keys in GOOGLE_API_KEY in settings.py
   - cd youtubeVideo
   - Run `docker-compose up --build` 
   - go to `http://localhost:8000/videos/` to access all the videos in order
   - go to `http://localhost:8000/admin/` to access admin panel
* ### Download code and run - 
    
    - `git clone https://github.com/pnshiralkar/youtube-videos-api.git`\
    - `cd youtube-videos-api`\
    - `pip install -r requirements.txt`
    - Run in 2 different terminals: `python manage.py syncYoutube` and `python manage.py runserver`

# What to do next
 - Setup YouTube data v3 API: [https://developers.google.com/youtube/v3/getting-started](https://developers.google.com/youtube/v3/getting-started)
 - Setup Search API reference: [https://developers.google.com/youtube/v3/docs/search/list](https://developers.google.com/youtube/v3/docs/search/list)
 - After setting up your localserver create super user to access admin panel in <base_url>/admin
 - View video dashboard in <base_url>/api

 

