from django.shortcuts import redirect

class RequireLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path in ['/hello/', '/update_server/', '/api/endpoints/']:
            return self.get_response(request)
        if not request.user.is_authenticated and request.path not in ['/accounts/login/', '/accounts/register/']:
            return redirect('register')
        if request.user.is_authenticated and request.path in ['/accounts/login/', '/accounts/register/']:
            return redirect('home')
        return self.get_response(request)
