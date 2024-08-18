from django.contrib.auth import authenticate, login  
from django.shortcuts import render, redirect  
from django.contrib import messages  
from tweets.models import UserProfile

def login_view(request):  
    if request.method == 'POST':  
        username = request.POST.get('username')  
        password = request.POST.get('password')  
        user = authenticate(request, username=username, password=password)  
        if user is not None:  
            login(request, user)  
            return redirect('home')  # Redirecione para a página inicial ou outra página desejada  
        else:  
            messages.error(request, 'Credenciais inválidas')  
    return render(request, 'login.html')  # Altere para o caminho do seu template de login

from django.contrib.auth.models import User  
from django.shortcuts import render, redirect  
from django.contrib import messages  

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            # Criar o usuário
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            
            # Criar o perfil do usuário
            user_profile = UserProfile.objects.create(user=user)
            
            # Autenticar e logar o usuário
            login(request, user)
            
            # Redirecionar para a página de perfil para adicionar mais informações
            return redirect('user_profile', username=user.username)
        else:
            messages.error(request, 'As senhas não coincidem')
    
    return render(request, 'register.html')  # Altere para o caminho do seu template de registro