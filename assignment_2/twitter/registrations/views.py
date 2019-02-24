from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, HttpResponse
from .forms import SignUpForm
from django.contrib.auth.models import User
from .models import Follower
from django.contrib.auth.decorators import login_required
from datetime import datetime
from tweets.models import Tweetlist
import json


def signup(request):
    """
    signup function for new user. function redirects to dashboard after authentication.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required(login_url='/login/')
def get_find_people_list(request):
    """
    :return: suggestion list of user whom requested user in not following
    """
    people_list = User.objects.all().exclude(
        id__in = Follower.objects.filter(follower= request.user, end__isnull=True).values_list('followee'))
    return render(request, "find_people.html", {'people_list':people_list})


@login_required(login_url='/login/')
def follow(request, id):
    """
    function creates link between follower and followee. if requested user has any past history with followee,
    function removes that data and recreates record
    """
    followee = User.objects.get(id=id)
    if Follower.objects.filter(follower=request.user, followee=followee).exists():
        print ("exsts")
        Follower.objects.filter(follower=request.user, followee=followee).delete()
    Follower.objects.create(follower=request.user, followee=followee, start=datetime.now())
    return redirect('/user_details/'+ followee.username)


@login_required(login_url='/login/')
def follower_list(request):
    """
    :return:  follower list of requested user
    """
    users_list = User.objects.filter(id__in=Follower.objects.filter(followee=request.user, end__isnull=True).values_list('follower'))
    return render(request, 'followers_list.html', {'users_list': users_list })


@login_required(login_url='/login/')
def following_list(request):
    """
    :return: list of following of request_user
    """
    users_list = User.objects.filter(id__in=Follower.objects.filter(follower=request.user, end__isnull=True).values_list('followee'))
    return render(request, 'following_list.html', {'users_list':users_list})


@login_required(login_url='/login/')
def unfollow(request, id):
    """
    :param id: user id to unfollow
    """
    Follower.objects.filter(follower=request.user, followee=User.objects.get(id=id)).update(end=datetime.now())
    return redirect('following_list')


def search_user(request):
    """
    :return: user list for seaching
    """
    search_user = User.objects.filter().exclude(id=request.user.id).values_list('username')
    search_user_list = [user[0] for user in search_user]
    return HttpResponse(json.dumps({'search_user_list':search_user_list}), content_type='application/json')


def user_details(request, username):
    """
    :return: usedeatails with past history of tweets or following if exists
    """
    userdetail = User.objects.get(username=username)
    following_details = Follower.objects.get(follower=request.user, followee=userdetail) if Follower.objects.filter(follower=request.user, followee=userdetail).exists() else {}
    tweets = Tweetlist.objects.filter(user_key=userdetail.id)
    return render(request, 'selected_user.html', {'userdetail': userdetail, 'following_details':following_details, 'tweets':tweets})