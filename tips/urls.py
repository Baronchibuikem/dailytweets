from django.urls import path
from tips.views import displayscheduledtweets, retweet_tip, displaytweets

app_name = "tips"

urlpatterns = [
    path('', displayscheduledtweets, name="home"),
    path('retweet/<int:id>/', retweet_tip, name="retweet"),
    path('post-tweets/', displaytweets, name="post-tweets")
]