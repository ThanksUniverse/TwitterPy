from django.shortcuts import render
from django.contrib.auth.models import User
from tweets.models import Tweet, UserProfile
from django.db.models import Q

def home(request):
    user_profile = UserProfile.objects.get(user=request.user)
    import pdb; pdb.set_trace()

    tweets = Tweet.objects.filter(Q(user__in=followed_users) | Q(user=request.user)).order_by('-created_at')
    
    return render(request, 'home.html', {'tweets': tweets})

def all_users(request):
    query = request.GET.get('q')
    if query:
        users = User.objects.filter(Q(username__icontains=query) | Q(userprofile__bio__icontains=query))
    else:
        users = User.objects.all()
    return render(request, 'all_users.html', {'users': users, 'query': query})


def followed_users(request):
    user_profile = UserProfile.objects.get(user=request.user)
    followed_users = user_profile.follows.all()

    query = request.GET.get('q')
    if query:
        followed_users = followed_users.filter(Q(user__username__icontains=query) | Q(bio__icontains=query))

    return render(request, 'followed_users.html', {'follows': followed_users, 'query': query})

