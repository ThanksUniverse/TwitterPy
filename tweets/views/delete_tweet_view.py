from django.shortcuts import get_object_or_404, redirect
from tweets.models import Tweet
from django.contrib.auth.decorators import login_required

@login_required
def delete_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id, user=request.user)
    tweet.delete()
    return redirect('user_profile', username=request.user.username)
