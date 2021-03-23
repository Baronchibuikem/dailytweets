from django.contrib import admin
from tips.models import DailyTip, TweetLinks

class DailyTipAdmin(admin.ModelAdmin):
    list_display = ["id","tip_id","timestamp", "posted_by","retweets","likes", "python_tip"]

admin.site.register(DailyTip, DailyTipAdmin)
admin.site.register(TweetLinks)

# Register your models here.
