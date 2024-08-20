def api_endpoints(request):
    endpoints = {
        'Home': '/',
        'Login': '/accounts/login/',
        'Register': '/accounts/register/',
        'Logout': '/logout/',
        'All Users': '/usuarios/',
        'Followed Users': '/seguindo/',
        'User Profile': '/perfil/<username>/',
        'Search Users': '/buscar/?q=<query>',
        'Follow/Unfollow User': '/seguir/<username>/',
        'Feed': '/?filter=feed',
        'Top Tweets': '/?filter=top',
    }
    return render(request, 'api_endpoints.html', {'endpoints': endpoints})
