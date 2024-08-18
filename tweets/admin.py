from django.contrib import admin

from .models import Tweet
from .models import UserProfile

admin.site.register(Tweet)
admin.site.register(UserProfile)
