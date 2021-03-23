# import native python libraries
import json

# import default django libraries


# import third party libraries
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.social_serializers import TwitterLoginSerializer

# import custom libraries here
from tips.models import PostDailyTip
from tips.api.serializers import PostDailyTipSerializer
from utils import tweepy_authourization




class TwitterLogin(SocialLoginView):
    """
    Used for Twitter API login. 
    You are expected to enter your:
    "access_token": "",
    "token_secret": ""

    if successfully authenticated, you will get key in return
    "key": ""
    """
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter


class PostTipView(generics.GenericAPIView):
    queryset = PostDailyTip.objects.all()
    serializer_class = PostDailyTipSerializer


    def post(self, request):

        validation_error = {
            "status": "failure",
            "reason": "something went wrong, please try again"
        }

        val_fail = False

        try:
            # get the tip from the request data
            content = request.data["python_tip"] 
            print(content, "serialized content")

            # get all the tips from the database
            all_tips = PostDailyTip.objects.all()
            
            # using list expression, loop over all_tips and get a single tip
            single_tip = [tip.python_tip for tip in all_tips]  
            
            # check if content ie request.data from the user is already in list of values from the datbase
            if content in single_tip:
                val_fail = True
                return Response({
                    "message": "Tip with same content already exist"
                }, status.HTTP_400_BAD_REQUEST) 

            if len(content) > 140:
                val_fail = True
                return Response(
                    {
                        "message": "content cannot be creater than 140 characters"
                    },
                status.HTTP_400_BAD_REQUEST 
            )
        # if there was an error in the serializer data
        except Exception as e:
            print(str(e), "EXCEPT")
            return Response(
                validation_error,
                status.HTTP_400_BAD_REQUEST
            ) 

        # check if the value of val_fail is True, if yes return the error message with 400 status code
        if val_fail:
            return Response(
                validation_error,
                status.HTTP_400_BAD_REQUEST
            )
        else:   
            # create the PostDailyTip instance and save
            daily_tip = PostDailyTip.objects.create(**request.data)
            daily_tip.save()
            return Response(
                (PostDailyTipSerializer(daily_tip)).data,
                status.HTTP_201_CREATED
            )
            

class DeleteTipView(generics.DestroyAPIView):
    """
    For deleting a specific tip
    """

    def destroy(self, request,id):
        status, obj = PostDailyTip.objects.filter(id=id).delete()
        if status == 1:
            return Response({
                "status": "success",
                "message": "Tip has successfully been deleted"
            })
        else:
            return Response({
                "status": "failure",
                "message": "could not delete tweet or tip does't not exist"
            })


class UpdateTipView(generics.UpdateAPIView):
    """
    For updating a specific tip
    """
    queryset = PostDailyTip.objects.all()
    serializer_class = PostDailyTipSerializer
    lookup_field = "id"



class RetrieveTipView(generics.RetrieveAPIView):
    """
    For retrieving a specific tip
    """
    queryset = PostDailyTip.objects.all()
    serializer_class = PostDailyTipSerializer
    lookup_field = "id"