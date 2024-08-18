from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from tweets.models import UserProfile, Tweet
from .forms import UserProfileForm

def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    user_profile, created = UserProfile.objects.get_or_create(user=user)
    
    tweets = Tweet.objects.filter(user=user).order_by('-created_at')

    is_owner = request.user == user_profile.user
    is_following = request.user.userprofile.follows.filter(pk=user_profile.pk).exists()

    if request.method == 'POST' and is_owner:
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile', username=username)
    else:
        form = UserProfileForm(instance=user_profile)

    context = {
        'user_profile': user_profile,
        'form': form,
        'tweets': tweets,
        'is_owner': is_owner,
        'is_following': is_following
    }
    return render(request, 'user_profile.html', context)
