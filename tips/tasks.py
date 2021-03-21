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
        # print(tweet.full_text)
        urls = tweet.entities["urls"]
        for url in urls:
            # print({
            #     "text": tweet.id
            # })
            # tweets_obj.append({
            #     "id": tweet.id,
            #     "python_tip":tweet.full_text,
            #     "posted_by" : tweet.user.name,
            #     "timestamp": tweet.created_at,
            #     "link__url": url["url"],
            #     "link__expanded_url": url["expanded_url"],
            #     "link__display_url": url["display_url"]
            # })
            # tweets_obj["id"] = tweet.id
            tweets_obj["python_tip"] = tweet.full_text
            tweets_obj["posted_by"] = tweet.user.name
            tweets_obj["timestamp"] = tweet.created_at
            tweets_obj["link__url"] = url["url"]
            tweets_obj["link__expanded_url"] = url["expanded_url"]
            tweets_obj["link__display_url"]= url["display_url"]
            print("----------------------------------",tweets_obj)
            tweets = DailyTip.tweets.create(
                    # id = tweets_obj["id"],
                    python_tip = tweets_obj["python_tip"],
                    posted_by =tweets_obj["posted_by"],
                    timestamp= tweets_obj["timestamp"],
                    url= tweets_obj["link__url"],
                    expanded_url= tweets_obj["link__expanded_url"] ,
                    display_url= tweets_obj["link__display_url"]
            )
            tweets.save()
            # return tweets_obj