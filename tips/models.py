from django.db import models


class Link(models.Model):
    url = models.URLField()
    expanded_url = models.URLField()
    display_url = models.URLField()

    def __str__(self):
        return self.url
    

class DailyTip(models.Model):
    python_tip = models.CharField(max_length=500)
    link = models.ForeignKey(Link, related_name="dailytips", on_delete=models.CASCADE)
    posted_by = models.CharField(max_length=100, blank=True)
    timestamp = models.DateField()
    tweets = models.Manager()

    def __str__(self):
        return self.posted_by
    
