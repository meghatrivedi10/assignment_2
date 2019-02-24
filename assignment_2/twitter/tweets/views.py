from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TweeetForm
from .models import Tweetlist


@login_required(login_url='/login/')
def add_tweet(request):
    """
    function to add tweet and redirect to dashboard
    """
    if request.method == 'POST':
        form = TweeetForm(request.POST)
        print (form)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.user_key = request.user
            form_data.save()
    return redirect('/')


@login_required(login_url='/login/')
def user_tweet(request):
    """
    :return: all the tweets of requested user
    """
    tweet_list = Tweetlist.objects.filter(user_key=request.user).order_by('-datetime')[:10]
    return render(request, 'all_tweets.html', {'tweet_list':tweet_list})