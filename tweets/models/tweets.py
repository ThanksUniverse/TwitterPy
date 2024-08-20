from django.db import models  
from django.contrib.auth.models import User  

class Tweet(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    content = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)  
    likes = models.ManyToManyField(User, related_name='liked_tweets', blank=True)
    image = models.ImageField(upload_to='tweet_images/', blank=True, null=True)

    def __str__(self):  
        return self.content

    def total_likes(self):
        return self.likes.count()
