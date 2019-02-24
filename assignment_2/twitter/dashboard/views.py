from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from tweets.forms import TweeetForm
from tweets.models import Tweetlist
from registrations.models import Follower
from django.db.models import Q


@login_required(login_url='/login/')
def dashboard(request):
    """
    :return: form to add tweet, most recent tweet list of the user and tweets from who user is following, total tweet count of user,
    followe count and followee count of user.
    """
    form = TweeetForm(request.POST)
    tweet_list = Tweetlist.objects.filter(Q(user_key__in= Follower.objects.filter(follower= request.user, end__isnull=True).values_list('followee')) | Q(user_key=request.user)).order_by('-datetime')[:10]
    tweet_count = Tweetlist.objects.filter(user_key = request.user).count()
    follower_count = Follower.objects.filter(followee= request.user, end__isnull=True).count()
    followee_count = Follower.objects.filter(follower=request.user, end__isnull=True).count()

    context = {'form':form, 'tweet_list':tweet_list, 'tweet_count':tweet_count, 'follower_count':follower_count,
               'followee_count':followee_count}

    return render(request, 'dashboard.html', context)

# from django.core import serializers
    # qs_json = serializers.serialize('json', tweet_list)
    # return HttpResponse(qs_json, content_type='application/json')