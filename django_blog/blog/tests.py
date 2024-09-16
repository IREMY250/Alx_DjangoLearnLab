# blog/tests.py

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AuthenticationTests(TestCase):
    def test_registration_view(self):
        response = self.client.get(reverse('blog:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/register.html')
    
    def test_login_view(self):
        response = self.client.get(reverse('blog:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/login.html')
