from django.shortcuts import render, redirect
from tweets.models import Tweet, UserProfile
from .forms import TweetForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required(login_url='register')
def home_view(request):
    if request.user.is_authenticated:
        # Formulário de criação de tweet
        if request.method == 'POST':
            form = TweetForm(request.POST)
            if form.is_valid():
                tweet = form.save(commit=False)
                tweet.user = request.user
                tweet.save()
                return redirect('home')
        else:
            form = TweetForm()

        # Obtendo o perfil do usuário autenticado
        user_profile = UserProfile.objects.get(user=request.user)

        # Obtendo os usuários que o usuário atual está seguindo
        followed_users = user_profile.follows.all().values_list('user', flat=True)

        # Filtrando os tweets desses usuários e do próprio usuário autenticado
        tweets = Tweet.objects.filter(Q(user__in=followed_users) | Q(user=request.user)).order_by('-created_at')
    else:
        # Se o usuário não estiver autenticado, exibe uma mensagem ou lista vazia
        form = None
        tweets = Tweet.objects.none()

    return render(request, 'home.html', {'form': form, 'tweets': tweets})
