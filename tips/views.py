#  django imports
from django.shortcuts import render

# third party imports


# custom imports
from tips.models import DailyTip



def displaytweets(request):    
    tweets = DailyTip.tweets.all()
    context = {
        "tweets": set(tweets)
    }
    template = "tips/tweet_list.html"
    return render(request, template, context)
    
