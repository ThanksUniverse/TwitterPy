from django.shortcuts import render, redirect  
from django.contrib.auth.decorators import login_required  
from .forms import TweetForm  
from tweets.models import Tweet  # Certifique-se de importar o modelo Tweet  

@login_required  
def create_tweet(request):  
    if request.method == 'POST':  
        form = TweetForm(request.POST)  
        if form.is_valid():  
            tweet = form.save(commit=False)  # Não salva ainda  
            tweet.user = request.user  # Associa o usuário autenticado  
            tweet.save()  # Agora salva o tweet  
            return redirect('home')  # Redireciona para a página inicial após criar o tweet  
    else:  
        form = TweetForm()  
    return render(request, 'create_tweet.html', {'form': form})