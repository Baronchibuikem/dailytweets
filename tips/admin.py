from django.contrib import admin
from tips.models import DailyTip, TweetLinks

class DailyTipAdmin(admin.ModelAdmin):
    list_display = ["id","tip_id","timestamp", "posted_by","retweets","likes", "python_tip"]

class TweetLinksAdmin(admin.ModelAdmin):
    list_display = ["id", "url", "expanded_url", "display_url"]

admin.site.register(DailyTip, DailyTipAdmin)
admin.site.register(TweetLinks, TweetLinksAdmin)

