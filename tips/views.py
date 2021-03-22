#  django imports
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# third party imports


# custom imports
from tips.models import DailyTip
from utils import tweepy_authourization


@login_required
def displaytweets(request):  
    # fetch all objects from DailyTip table in the database  
    tweets = DailyTip.objects.all()

    # used for search functionality
    query = request.GET.get("q")
    if query:
        tweets = tweets.filter(Q(python_tip__icontains=query)).distinct()

    # for pagination
    paginator = Paginator(tweets, 20)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)
    
    # context dictionary
    context = {
        "tweets": page_obj
    }
    template = "tips/tweet_list.html"
    return render(request, template, context)


    
@login_required
def retweet_tip(request, id):
    # get the ID of the tweet from the url parameter
    try:
        # get our tweepy authentication
        api = tweepy_authourization.tweep_auth()        
        # make a post request to retweet the tweet with the specified ID
        api.retweet(id)
        return HttpResponse("You have Retweeted the tip successfully")
    except:
        return HttpResponse("something went wrong. please try again")

    
    