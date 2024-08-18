from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from tweets.models import UserProfile

def follow_user(request, username):
    target_user = get_object_or_404(User, username=username)
    target_user_profile = get_object_or_404(UserProfile, user=target_user)
    user_profile = request.user.userprofile

    if target_user_profile in user_profile.follows.all():
        user_profile.follows.remove(target_user_profile)
    else:
        user_profile.follows.add(target_user_profile)
    
    return redirect('user_profile', username=username)
