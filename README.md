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
   - Setup YouTube data v3 API: [https://developers.google.com/youtube/v3/getting-started](https://developers.google.com/youtube/v3/getting-started)
   - Setup Search API reference: [https://developers.google.com/youtube/v3/docs/search/list](https://developers.google.com/youtube/v3/docs/search/list)
   - put api keys under settings.py in GOOGLE_API_KEYS field ( We can retrive it from .env but for current use you can put it in settings.py)
   
* ## Using Docker - 
   **Make sure you have docker and docker-compose installed. If not, refer: https://docs.docker.com/install/**

   - cd youtubeVideo
   - Run `docker-compose up --build` 
   - go to `http://localhost:8000/videos/` to access all the videos in order
   - go to `http://localhost:8000/admin/` to access admin panel
* ### Download code and run - 
    
    - `git clone https://github.com/pnshiralkar/youtube-videos-api.git`\
    - `cd youtube-videos-api`\
    - `pip install -r requirements.txt`
    - Run in 2 different terminals: `python manage.py runserver_with_sync`

# Routes

 - After setting up your localserver create super user to access admin panel in <base_url>/admin
 - View video dashboard in <base_url>/api
 - Search video in db here <base_url>/api/?search=das
 
# Screenshot

## Dashboard
![Screenshot 2022-11-05 at 2 55 27 AM](https://user-images.githubusercontent.com/52108435/200112005-b2ef95c9-9f07-49dd-8279-7dc34d19a422.png)

## Features
![Screenshot 2022-11-05 at 2 55 34 AM](https://user-images.githubusercontent.com/52108435/200112009-36e8777e-2b86-4b14-a91d-c19ecea9c34b.png)

## Admin Panel
 ![Screenshot 2022-11-05 at 2 55 53 AM](https://user-images.githubusercontent.com/52108435/200112012-ce437b85-f8fc-4e84-a0ce-f03134a8d82a.png)


