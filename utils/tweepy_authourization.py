# import django libraries
from django.conf import settings


# import third party libraries
import tweepy


def tweep_auth():
    # twitter authentication for application using tweepy
    auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api