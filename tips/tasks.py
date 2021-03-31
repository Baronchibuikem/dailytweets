# import django libraries
from django.core.mail import EmailMessage
from django.conf import settings

# import third party libraries
from celery.utils.log import get_task_logger
import tweepy

# import custom built libraries
from dailytips.celery import app
from tips.models import DailyTip,TweetLinks
from utils import tweepy_authourization, get_tweets



logger = get_task_logger(__name__)


@app.task
def get_daily_tips():
    get_tweets.fetch_tweets_and_save_to_db()