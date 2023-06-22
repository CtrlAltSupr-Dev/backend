from django.test import TestCase, Client
import unittest

from api.models import CustomUser

class SimpleTest(unittest.TestCase):
    def test_register(self):
        client = Client()
        response = client.post("/register/", {"username": "felipegalan", "email": "galan@uc.cl", "password1": "12345678", "password2": "12345678"})
        print(response)
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        client = Client()
        CustomUser.objects.create(username="alelopez", email="lopez@uc.cl", password="12345678", is_active=True, is_staff=False, is_superuser=False, email_verified=True)
        response = client.post("/login/", {"username": "alelopez", "password": "12345678"})
        self.assertEqual(response.status_code, 201)

"""
class CustomUserTestCase(TestCase):
    def setUp(self):
        CustomUser.objects.create(username="felipegalan", email="galan@uc.cl", password="12345678", is_active=True, is_staff=False, is_superuser=False, email_verified=True)
        CustomUser.objects.create(username="alelopez", email="lopez@uc.cl", password="12345678", is_active=True, is_staff=False, is_superuser=False, email_verified=True)

    def test_animals_can_speak(self):
        felipegalan = CustomUser.objects.get(username="felipegalan")
        alelopez = CustomUser.objects.get(username="alelopez")
        self.assertEqual(felipegalan.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
"""