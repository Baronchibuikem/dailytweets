from django.db import models


class CustomUser(models.Model):
    pass



class DailyTip(models.Model):
    python_tip = models.CharField(max_length=500)
    link = models.URLField()
    posted_by = models.CharField(max_length=100)
    published = models.CharField(max_length=50)
    timestamp = models.DateField()
    tweets = models.Manager()

    def __str__(self):
        return self.posted_by
    
