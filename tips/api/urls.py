from django.urls import path
from tips.api.viewsets import PostTipView, DeleteTipView, UpdateTipView,RetrieveTipView, TwitterLogin


app_name = "tips-api"
urlpatterns = [
    path("", PostTipView.as_view(), name="post-tip"),
    path("<int:id>/", DeleteTipView.as_view(), name="delete-tip"),
    path("<int:id>/update/", UpdateTipView.as_view(), name="update-tip"),
    path("<int:id>/get/", RetrieveTipView.as_view(), name="retrieve-tip"),
    path('login/twitter/', TwitterLogin.as_view(), name='twitter_login')
]
