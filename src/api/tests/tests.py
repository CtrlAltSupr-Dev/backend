from django.test import TestCase, Client
import unittest

from api.models import CustomUser

class SimpleTest(unittest.TestCase):
    def test_register_fail_password2(self):
        client = Client()
        response = client.post("/register/", {
            "username": 'felipegalan',
            "email": "galan@uc.cl",
            "password1": "animated.13"})
        print(response)
        self.assertEqual(response.status_code, 400)

    def test_register_fail_email(self):
        client = Client()
        response = client.post("/register/", {
            "username": 'felipegalan',
            "email": "galan@gmail.com",
            "password1": "animated.13",
            "password2": "animated.13"})
        print(response)
        self.assertEqual(response.status_code, 400)
    
    def test_register_pass(self):
        client = Client()
        response = client.post("/register/", {
            'username': 'felipegalan',
            'email': 'galan@uc.cl',
            'password1': 'animated.13',
            'password2': 'animated.13'
        })
        print(response)
        CustomUser.objects.filter(username="felipegalan").delete()
        self.assertEqual(response.status_code, 200)  # Cambia el status_code esperado a 200 si el registro es exitoso

'''

    def test_login_fail(self):
        client = Client()
        response = client.post("/login/", {"username": "felipegalan", "password": "wrongpassword"})
        CustomUser.objects.filter(username="felipegalan").delete()
        self.assertEqual(response.status_code, 400)

    def test_login_pass(self):
        client = Client()
        response = client.post("/login/", {"username": "alelopez", "password": "12345678"})
        CustomUser.objects.filter(username="alelopez").delete()
        self.assertEqual(response.status_code, 201)

'''

'''
class CustomUserTestCase(TestCase):
    def setUp(self):
        CustomUser.objects.create(username="felipegalan", email="galan@uc.cl", password="12345678", is_active=True, is_staff=False, is_superuser=False, email_verified=True)
        CustomUser.objects.create(username="alelopez", email="lopez@uc.cl", password="12345678", is_active=True, is_staff=False, is_superuser=False, email_verified=True)

    def test_login(self):
        c = Client()
        logged_in = c.login(username='felipegalan', password='12345678')
        self.assertTrue(logged_in)
'''
