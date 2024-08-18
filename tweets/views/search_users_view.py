from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.models import User

def search_users(request):
    query = request.GET.get('q')
    users = User.objects.filter(Q(username__icontains=query) | Q(userprofile__bio__icontains=query))
    return render(request, 'search_results.html', {'users': users, 'query': query})
