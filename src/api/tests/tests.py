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

    def test_login_fail_password(self):
        client = Client()
        client.post("/register/", {
            'username': 'felipegalan',
            'email': 'galan@uc.cl',
            'password1': 'animated.13',
            'password2': 'animated.13'
        })
        CustomUser.objects.filter(username="felipegalan").update(email_verified=True, is_active=True)
        response = client.post("/login/", {"username": "felipegalan", "password": "wrongpassword"})
        print(response)
        CustomUser.objects.filter(username="felipegalan").delete()
        self.assertEqual(response.status_code, 401)

    def test_login_fail_confirmation(self):
        client = Client()
        client.post("/register/", {
            'username': 'felipegalan',
            'email': 'galan@uc.cl',
            'password1': 'animated.13',
            'password2': 'animated.13'
        })
        response = client.post("/login/", {"username": "felipegalan", "password": "wrongpassword"})
        print(response)
        CustomUser.objects.filter(username="felipegalan").delete()
        self.assertEqual(response.status_code, 400)

    def test_login_pass(self):
        client = Client()
        client.post("/register/", {
            'username': 'felipegalan',
            'email': 'galan@uc.cl',
            'password1': 'animated.13',
            'password2': 'animated.13'
        })
        CustomUser.objects.filter(username="felipegalan").update(email_verified=True, is_active=True)
        response = client.post("/login/", {"username": "felipegalan", "password": "animated.13"})
        print(response)
        CustomUser.objects.filter(username="felipegalan").delete()
        self.assertEqual(response.status_code, 200)
