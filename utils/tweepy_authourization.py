# import django libraries
from django.conf import settings

# import third party libraries
import tweepy




# because we will be using this tweet authentication in more than one place, we had to make it a
# utility function so we can import and instantiate it from anywhere in our codebase
def tweep_auth():
    # twitter authentication for application using tweepy
    auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth) #api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    return api