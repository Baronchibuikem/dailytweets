from django.urls import path
from tips.views import displaytweets

app_name = "tips"

urlpatterns = [
    path('', displaytweets, name="daily-tweets"),
]