from django.db import models


class TweetLinks(models.Model):
    url = models.URLField()
    expanded_url = models.URLField()
    display_url = models.URLField()

class DailyTip(models.Model):
    id = models.AutoField(primary_key=True)
    tip_id = models.IntegerField()
    python_tip = models.TextField(max_length=500)
    posted_by = models.CharField(max_length=100, blank=True)
    timestamp = models.DateField()
    #formart = url1,expanded_url1,name1;url2,expanded_url2,name2
    urls = models.ManyToManyField(TweetLinks)
    likes = models.IntegerField()
    retweets = models.IntegerField()
    # tweets = models.Manager()


    class Meta:
        ordering = ["-likes"]

        
    def __str__(self):
        return self.posted_by
    
