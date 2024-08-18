from django.test import TestCase
from django.contrib.auth.models import User
from tweets.models import Tweet, UserProfile

class TweetTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user_profile, created = UserProfile.objects.get_or_create(user=self.user)
        self.tweet = Tweet.objects.create(user=self.user, content="Este é um tweet de teste")

    def test_tweet_creation(self):
        self.assertEqual(self.tweet.content, "Este é um tweet de teste")
        self.assertEqual(self.tweet.user.username, 'testuser')

    def test_user_profile_creation(self):
        self.assertEqual(self.user_profile.user.username, 'testuser')

    def test_home_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Este é um tweet de teste")
