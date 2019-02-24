

from django.urls import path
from . import views

urlpatterns = [
    path('find_people/', views.get_find_people_list, name="get_find_people_list"),
    path('follow/<id>', views.follow, name="follow"),
    path('follower_list', views.follower_list, name="follower_list"),
    path('following_list', views.following_list, name="following_list"),
    path('unfollow/<id>', views.unfollow, name="unfollow"),
    path('search_user', views.search_user, name="search_user"),
    path('user_details/<username>', views.user_details, name="user_details"),
]