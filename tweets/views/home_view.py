from django.shortcuts import render, redirect
from tweets.models import Tweet, UserProfile
from .forms import TweetForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required(login_url='register')
def home_view(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('home')
    else:
        form = TweetForm()

    user_profile = UserProfile.objects.get(user=request.user)

    followed_users = user_profile.follows.all().values_list('user', flat=True)

    tweets = Tweet.objects.filter(Q(user__in=followed_users) | Q(user=request.user)).order_by('-created_at')

    total_tweets = Tweet.objects.count()

    if not tweets.exists():
        no_tweets_message = "Ainda não há tweets no seu feed. Siga alguém ou faça um post para começar a ver os posts."
    else:
        no_tweets_message = None

    return render(request, 'home.html', {
        'form': form,
        'tweets': tweets,
        'total_tweets': total_tweets,
        'no_tweets_message': no_tweets_message,
    })
