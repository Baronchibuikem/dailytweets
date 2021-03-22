from django.urls import path
from tips.views import displaytweets, retweet_tip

app_name = "tips"

urlpatterns = [
    path('', displaytweets, name="home"),
    path('retweet/<int:id>/', retweet_tip, name="retweet")
]