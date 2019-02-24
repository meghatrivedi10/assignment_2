from django.urls import path
from . import views


urlpatterns = [
    path('save/', views.add_tweet, name="add_tweet"),
    path('list/', views.user_tweet, name="user_tweet"),
]