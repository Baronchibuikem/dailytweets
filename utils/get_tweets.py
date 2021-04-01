# import django libraries
from django.core.mail import EmailMessage
from django.conf import settings

# import third party libraries
import tweepy

# import custom libraries
from tips.models import DailyTip, TweetLinks
from utils import tweepy_authourization



def fetch_tweets_and_save_to_db(request):
    api = tweepy_authourization.tweep_auth()
    
    timeline = None

    # check if DB contains saved tweets ordered by their timestamp, if it does, get the last tweet
    last_tweet = DailyTip.objects.all().order_by('timestamp').last()

    # if the value of last_tweet is None exclude the "since_id" from the parameters you are passing to user_timeline
    if last_tweet == None:
        print("No tweet found. We are running this for the first time")

        # id: the name of the user whose timeline we want to get
        # count: maximum allowed tweets count
        # tweet_mode: extended to get the full text,it prevents a primary tweet longer than 140 characters from being truncated.
        # exclude_replies: this will prevent replies from appearing in the returned timeline. 
        timeline = api.user_timeline(
            id=settings.TWITTER_USER,
            count=settings.NUMBER_OF_TWEETS,
            tweet_mode="extended",
            exclude_replies=True
        )
    # if the value of last_tweet is not none, we will include the "since_id" parameter
    else:
        print("Displaying the ID of the last saved tweet",last_tweet.id)

        # id: the name of the user whose timeline we want to get
        # count: maximum allowed tweets count
        # tweet_mode: extended to get the full text,it prevents a primary tweet longer than 140 characters from being truncated.
        # exclude_replies: this will prevent replies from appearing in the returned timeline. 
        # since_id: returns only statuses with an ID greater than (that is, more recent than) the specified ID
        timeline = api.user_timeline(
            id=settings.TWITTER_USER,
            count=settings.NUMBER_OF_TWEETS,
            tweet_mode="extended",
            exclude_replies=True,
            since_id = last_tweet.tip_id
        )
    
    # will be used to populate our tweet objects
    tweets_obj = {}

    # we check if the length of our timeline is greater than zero, which means we have existing tweets
    if len(timeline)!=0:
        for tweet in timeline:
            # we get all links attached to a tweet tip
            urls = tweet.entities["urls"]
            
            # adding the tweet objects to our empty tweet_obj dictionary
            tweets_obj["python_tip"] = tweet.full_text
            tweets_obj["posted_by"] = tweet.user.name
            tweets_obj["timestamp"] = tweet.created_at
            tweets_obj["retweets"] = tweet.retweet_count
            tweets_obj['likes'] = tweet.favorite_count
            tweets_obj["id"] = tweet.id

            # saving the values in our tweet_obj to our DailyTip table
            tweets = DailyTip(
                    python_tip = tweets_obj["python_tip"],
                    posted_by =tweets_obj["posted_by"],
                    timestamp= tweets_obj["timestamp"],
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
        print("No new tweet has been added")

class Tweets:
    def __init__(self):
        self.tweets_obj = []

    
    def fetch_tweets(self, username = None):
        api = tweepy_authourization.tweep_auth()
        
        timeline = None

        # will be used to populate our tweet objects
        twe_obj = {"id": 1, "name": "Andy"}

        # check if DB contains saved tweets ordered by their timestamp, if it does, get the last tweet
        last_tweet = DailyTip.objects.all().order_by('timestamp').last()

        # if the value of last_tweet is None exclude the "since_id" from the parameters you are passing to user_timeline
        if last_tweet == None:
            print("No tweet found. We are running this for the first time")

            # id: the name of the user whose timeline we want to get
            # count: maximum allowed tweets count
            # tweet_mode: extended to get the full text,it prevents a primary tweet longer than 140 characters from being truncated.
            # exclude_replies: this will prevent replies from appearing in the returned timeline. 
            timeline = api.user_timeline(
                id=username,
                count=settings.NUMBER_OF_TWEETS,
                tweet_mode="extended",
                exclude_replies=True
            )
        # if the value of last_tweet is not none, we will include the "since_id" parameter
        else:
            print("Displaying the ID of the last saved tweet",last_tweet.id)

            # id: the name of the user whose timeline we want to get
            # count: maximum allowed tweets count
            # tweet_mode: extended to get the full text,it prevents a primary tweet longer than 140 characters from being truncated.
            # exclude_replies: this will prevent replies from appearing in the returned timeline. 
            # since_id: returns only statuses with an ID greater than (that is, more recent than) the specified ID
            timeline = api.user_timeline(
                id=settings.username,
                count=settings.NUMBER_OF_TWEETS,
                tweet_mode="extended",
                exclude_replies=True,
                since_id = last_tweet.tip_id
            )
        

        tweet_obj = []
        # we check if the length of our timeline is greater than zero, which means we have existing tweets
        if len(timeline)!=0:
            for tweet in timeline:
                urls = tweet.entities["urls"]

                if len(urls)!=0:
                    for url in urls:
                        tweet_obj.append({
                            "url" : url["url"],
                            "expanded_url" : url["expanded_url"],
                            "display_url" : url["display_url"]
                        })
                    print("TWEEEEEEEEEEEEEE", tweet_obj)    
                self.tweets_obj.append({
                    "text": tweet.full_text,
                    "posted_by": tweet.user.name,
                    "timestamp": tweet.created_at,
                    "retweets": tweet.retweet_count,
                    "likes": tweet.favorite_count,
                    "tweet_id": tweet.id,
                   
                    })
                                
                        
        else:
            print("No new tweet has been added")
        

    @property
    def tweet_callback(self):
        return self.tweets_obj
    