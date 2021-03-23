#  django imports
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

# third party imports


# custom imports
from tips.models import DailyTip



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
    
