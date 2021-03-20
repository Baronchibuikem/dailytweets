# import django libraries
from django.core.mail import EmailMessage
from django.conf import settings

# import third party libraries
from celery.utils.log import get_task_logger
import tweepy

# import custom built libraries
from dailytips.celery import app
from tips.models import DailyTip



logger = get_task_logger(__name__)

# twitter authentication for application using tweepy
auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


@app.task
def get_daily_tips():
    logger.info("Starting job")
    python_tip_account = api.get_user("python_tip")
    logger(python_tip_account)
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)
    # new_tweet = DailyTip(
    #     "python_tip": "value",
    #     "link": "value",
    #     "posted_by" : "value",
    #     "published": "value",
    #     "timestamp": "value"
    # )
    # new_tweet.save()
    logger.info("New tweet has been saved to the database")
    return new_tweet