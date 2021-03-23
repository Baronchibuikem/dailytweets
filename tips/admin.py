from django.contrib import admin
from tips.models import DailyTip, TweetLinks, PostDailyTip

class DailyTipAdmin(admin.ModelAdmin):
    list_display = ["id","tip_id","timestamp", "posted_by","retweets","likes", "python_tip"]

class TweetLinksAdmin(admin.ModelAdmin):
    list_display = ["id", "url", "expanded_url", "display_url"]

class PostDailyTipAdmin(admin.ModelAdmin):
    list_display = ["id", 'python_tip', 'your_twitter_name', 'your_email']

admin.site.register(DailyTip, DailyTipAdmin)
admin.site.register(TweetLinks, TweetLinksAdmin)
admin.site.register(PostDailyTip, PostDailyTipAdmin)

