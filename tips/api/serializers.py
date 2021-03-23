from rest_framework import serializers
from tips.models import PostDailyTip


class PostDailyTipSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostDailyTip
        fields = ("python_tip", "your_twitter_name", "your_email")

        




