# import django libraries
from django.core.mail import EmailMessage
from django.conf import settings
import json,pprint

# import third party libraries
from celery.utils.log import get_task_logger
import tweepy

# import custom built libraries
from dailytips.celery import app
from tips.models import DailyTip,TweetLinks



logger = get_task_logger(__name__)



@app.task
def get_daily_tips():
    # twitter authentication for application using tweepy
    auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    #CHECK IF ANY TWEETS IN DB
    #AND GET THE LAST ordered by timestamp
    timeline = None
    last_tweet = DailyTip.objects.all().order_by('timestamp').last()
    if last_tweet == None:
        print("NO LAST TWEET, FIRST TIME RUNNING")
        #count: maximum allowed tweets count
        #tweet_mode: extended to get the full text,it prevents a primary tweet longer than 140 characters from being truncated.
        timeline = api.user_timeline(
            id=settings.TWITTER_USER,
            count=settings.NUMBER_OF_TWEETS,
            tweet_mode="extended",
            exclude_replies=True
        )
    else:
        print("LAST TWEET",last_tweet.id)
        timeline = api.user_timeline(
            id=settings.TWITTER_USER,
            count=settings.NUMBER_OF_TWEETS,
            tweet_mode="extended",
            exclude_replies=True,
            since_id = last_tweet.tip_id
        )
    
    # will be used to populate our tweet objects
    tweets_obj = {}

    if len(timeline)!=0:
        for tweet in timeline:
            # pprint.pprint(tweet)
            urls = tweet.entities["urls"]
        
            print({
                "text": tweet.id
            })
            # composed_url = ""
            # if len(urls)!=0:
            #     for url in urls:
            #         composed_url = composed_url+"{},{},{};".format(
            #             url["url"],
            #             url["expanded_url"],
            #             url["display_url"]
            #         )
        
            
            # adding the tweet objects to our empty tweet_obj dictionary
            tweets_obj["python_tip"] = tweet.full_text
            tweets_obj["posted_by"] = tweet.user.name
            tweets_obj["timestamp"] = tweet.created_at
            #tweets_obj["urls"] = composed_url
            #tweets_obj["expanded_url"] = url["expanded_url"]
            #tweets_obj["display_url"]= url["display_url"]
            tweets_obj["retweets"] = tweet.retweet_count + 1
            tweets_obj['likes'] = tweet.favorite_count
            tweets_obj["id"] = tweet.id

            # saving the values in our tweet_obj to our DailyTip table
            # print(tweets_obj)
            tweets = DailyTip(
                    python_tip = tweets_obj["python_tip"],
                    posted_by =tweets_obj["posted_by"],
                    timestamp= tweets_obj["timestamp"],
                    #urls= tweets_obj["urls"],
                    # expanded_url= tweets_obj["expanded_url"] ,
                    # display_url= tweets_obj["display_url"],
                    retweets= tweets_obj["retweets"],
                    likes = tweets_obj["likes"],
                    tip_id = tweets_obj["id"]
            )
            tweets.save()

            if len(urls)!=0:
                for url in urls:
                    tweetlink=TweetLinks(
                        url=url["url"],
                        expanded_url=url["expanded_url"],
                        display_url=url["display_url"]
                    )
                    tweetlink.save()
                    tweets.urls.add(tweetlink)
    else:
        print("NO TWEET YET")