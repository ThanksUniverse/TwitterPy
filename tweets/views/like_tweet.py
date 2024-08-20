from django.shortcuts import render, redirect, get_object_or_404
from tweets.models import Tweet
from django.contrib.auth.decorators import login_required

@login_required
def like_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    if request.user in tweet.likes.all():
        tweet.likes.remove(request.user)
    else:
        tweet.likes.add(request.user)
    return redirect('home')
