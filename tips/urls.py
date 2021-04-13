from django.urls import path
from tips.views import displayscheduledtweets, retweet_tip, displaytweets

app_name = "tips"

urlpatterns = [
    path('', displaytweets, name="post-tweets"),
    path('s/', displayscheduledtweets, name="home"),
    path('retweet/<int:id>/', retweet_tip, name="retweet"),
]