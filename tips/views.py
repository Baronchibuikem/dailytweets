#  django imports
from django.shortcuts import render

# third party imports


# custom imports
from tips.models import DailyTip



def displaytweets(request):
    
    # tweets = DailyTip.events.all()
    context = {
        "tweets": "tweets"
    }
    template = "tips/tweet_list.html"
    return render(request, template, context)
    
