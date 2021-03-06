# import native python libraries
from datetime import date

# import django libraries
from django.db import models

# import third party libraries


# import custom libraries

    

class PostDailyTip(models.Model):
    """
    For uploading our own tips into the database
    """
    id = models.AutoField(primary_key=True)
    python_tip = models.CharField(max_length=140)
    your_twitter_name = models.CharField(max_length=140)
    your_email = models.EmailField()


    def __str__(self):
        return self.python_tip

# models for saving our links
class TweetLinks(models.Model):
    """
    This table is used to hold links attached to a specific tweet
    """
    url = models.URLField()
    expanded_url = models.URLField()
    display_url = models.URLField()

    def __str__(self):
        return self.display_url
    

class DailyTip(models.Model):
    """
    This table is used for storing our data being returned when we run our celery to fetch tweets from a user's timeline
    """
    id = models.AutoField(primary_key=True)
    tip_id = models.IntegerField()
    python_tip = models.TextField(max_length=500)
    posted_by = models.CharField(max_length=100, blank=True)
    timestamp = models.DateField()
    urls = models.ManyToManyField(TweetLinks)
    likes = models.IntegerField()
    retweets = models.IntegerField()


    class Meta:
        ordering = ["-likes"]

        
    def __str__(self):
        return self.posted_by
    
