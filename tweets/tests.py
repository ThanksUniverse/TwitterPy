from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
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

    def test_user_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpass',
            'confirm_password': 'newpass',
        })
        self.assertEqual(response.status_code, 302)  

        new_user = User.objects.filter(username='newuser').exists()
        self.assertTrue(new_user)

        new_user_profile = UserProfile.objects.filter(user__username='newuser').exists()
        self.assertTrue(new_user_profile)

    def test_user_login(self):
        self.client.logout()  
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertEqual(response.status_code, 302)  

        user = User.objects.get(username='testuser')
        self.assertTrue(user.is_authenticated)

    def test_user_login_with_invalid_credentials(self):
        self.client.logout()  
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrongpass'
        })
        self.assertEqual(response.status_code, 200)  
        self.assertContains(response, 'Credenciais inválidas')

    def test_duplicate_user_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'newpass',
            'confirm_password': 'newpass',
        })
        self.assertEqual(response.status_code, 302)  # Agora esperamos um redirecionamento

        messages = list(response.wsgi_request._messages)
        self.assertTrue(any("Usuário já existe" in str(message) for message in messages))

