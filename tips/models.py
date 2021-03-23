from django.db import models


# models for saving our links
class TweetLinks(models.Model):
    url = models.URLField()
    expanded_url = models.URLField()
    display_url = models.URLField()

    def __str__(self):
        return self.display_url
    

class DailyTip(models.Model):
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
    
