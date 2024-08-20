from django.contrib import admin
from django.urls import path, include
from tweets.views import login_view, register_view, home_view
from tweets.views.home import home, all_users, followed_users
from django.contrib.auth.views import LogoutView
from tweets.views.search_users_view import search_users
from tweets.views.user_view import user_profile
from django.conf import settings
from django.conf.urls.static import static
from tweets.views.follow_user_view import follow_user
from tweets.views.api_endpoints import api_endpoints
from tweets.views.delete_tweet_view import delete_tweet
from tweets.views.pythonanywhere_view import update, hello_world
from tweets.views.like_tweet import like_tweet

urlpatterns = [
    path("admin/", admin.site.urls),
    path('tweets/', include('tweets.urls')), 
    path('accounts/login/', login_view, name='login'), 
    path('accounts/register/', register_view, name='register'), 
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'), 
    path('usuarios/', all_users, name='all_users'),
    path('seguindo/', followed_users, name='followed_users'),
    path('perfil/<str:username>/', user_profile, name='user_profile'),
    path('buscar/', search_users, name='search_users'),
    path('seguir/<str:username>/', follow_user, name='follow_user'),
    path('tweet/delete/<int:tweet_id>/', delete_tweet, name='delete_tweet'),
    path('like/<int:tweet_id>/', like_tweet, name='like_tweet'),
    path('api/endpoints/', api_endpoints, name='api_endpoints'),
    path('update_server/', update, name='update_server'),
    path("hello/", hello_world, name="hello_world"),
    path('', home_view, name='home'),   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
