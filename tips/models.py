from django.db import models


class DailyTip(models.Model):
    id = models.AutoField(primary_key=True)
    python_tip = models.TextField(max_length=500)
    posted_by = models.CharField(max_length=100, blank=True)
    timestamp = models.DateField()
    url = models.URLField()
    expanded_url = models.URLField()
    display_url = models.URLField()
    likes = models.CharField(max_length=999999, blank=True, default="")
    retweets = models.CharField(max_length=999999, blank=True, default="")
    tweets = models.Manager()

    def __str__(self):
        return self.posted_by
    
