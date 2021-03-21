# import django libraries
from django.core.mail import EmailMessage
from django.conf import settings
import json

# import third party libraries
from celery.utils.log import get_task_logger
import tweepy

# import custom built libraries
from dailytips.celery import app
from tips.models import DailyTip



logger = get_task_logger(__name__)



@app.task
def get_daily_tips():
    # twitter authentication for application using tweepy
    auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    #count: maximum allowed tweets count
    #tweet_mode: extended to get the full text,it prevents a primary tweet longer than 140 characters from being truncated.
    timeline = api.user_timeline(id=settings.TWITTER_USER, count=settings.NUMBER_OF_TWEETS,tweet_mode="extended")
    
    tweets_obj = {}
    # Iterate and print tweets
    # textonly_tweets = [tweet.full_text for tweet in timeline]
    # print(*textonly_tweets, sep = "\n")
    for tweet in timeline:
        # print(tweet)
        urls = tweet.entities["urls"]
        for url in urls:
            # print({
            #     "text": tweet.id
            # })
            DailyTip({
                "id": tweet.id,
                "python_tip":tweet.full_text,
                "posted_by" : tweet.user.name,
                "timestamp": tweet.created_at,
                "link__url": url["url"],
                "link__expanded_url": url["expanded_url"],
                "link__display_url": url["display_url"]
            }).save()
        # tweet_obj = {
        #     "text": tweet.full_text,
        #     "timestamp": tweet.created_at,
        #     "urls": tweet.entities,

        # }
        # print(tweet_obj, sep="\n")

    # new_tweet = DailyTip(
    #     "python_tip": python_tip_account.name
    #     "link": "value",
    #     "posted_by" : python_tip_account.screen_name
    #     "published": "value",
    #     "timestamp": "value"
    # )
    # new_tweet.save()

# [{
#     'url': 'https://t.co/4TRTgGhwGt', 
#     'expanded_url': 'https://resources.rstudio.com/resources/rstudioglobal-2021/using-pins-with-python-and-javascript/', 
#     'display_url': 'resources.rstudio.com/resources/rstu…', 
#     'indices': [112, 135]
#     }
#     ]

# {'hashtags': [], 'symbols': [], 
# 'user_mentions': 
# [{'screen_name': 'gvanrossum', 'name': 'Guido van Rossum', 'id': 15804774, 'id_str': '15804774',
#  'indices': [77, 88]}
# ],
#  'urls': [
# {'url': 'https://t.co/BphxIqN4SA', 
#  'expanded_url': 'https://github.com/gvanrossum/patma/blob/master/README.md#tutorial', 
#  'display_url': 'github.com/gvanrossum/pat…', 'indices': [91, 114]}, 
#  {'url': 'https://t.co/tEvrIzAzhH', 
#  'expanded_url': 'https://twitter.com/gvanrossum/status/1361124478671933443', 
#  'display_url': 'twitter.com/gvanrossum/sta…', 
#  'indices': [115, 138]}]}