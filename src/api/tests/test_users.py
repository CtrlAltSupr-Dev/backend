from django.test import TestCase, Client

from api.models import CustomUser


class UserTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    # Get All
    def test_get_all_succesfull(self):
        CustomUser.objects.create(username="felipegalan", email="galan@uc.cl", password="12345678", is_active=True, is_staff=False, is_superuser=False, email_verified=True).save()
        response = self.client.get('/api/users')

        self.assertNotEqual(len(response.data), 0)
        self.assertEqual(response.status_code, 200)

    def test_get_all_unsuccesfull_no_teachers(self):
        CustomUser.objects.all().delete()
        response = self.client.get('/api/users')

        self.assertEqual(len(response.data), 0)

    # Get
    def test_get_succesfull(self):
        CustomUser.objects.create(username="felipegalan", email="galan@uc.cl", password="12345678", is_active=True, is_staff=False, is_superuser=False, email_verified=True).save()
        id = CustomUser.objects.all().last().id
        response = self.client.get(f'/api/users/details/{id}')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], 'felipegalan')
        self.assertEqual(response.data['email'], 'galan@uc.cl')

    def test_get_unsuccesfull_does_not_exist(self):
        CustomUser.objects.all().delete()
        response = self.client.get(f'/api/users/details/{1}')

        self.assertEqual(response.status_code, 404)

    # Delete
    def test_delete_succesfull(self):
        id = CustomUser.objects.all().last().id
        response = self.client.delete(f'/api/users/delete/{id}')

        self.assertEqual(response.status_code, 204)

    def test_delete_unsuccesfull_does_not_exist(self):
        CustomUser.objects.all().delete()
        response = self.client.delete('/api/users/delete/1')

        self.assertEqual(response.status_code, 404)

    # Update
    def test_update_succesfull(self):
        CustomUser.objects.create(username="felipegalan", email="galan@uc.cl", password="12345678", is_active=True, is_staff=False, is_superuser=False, email_verified=True).save()
        id = CustomUser.objects.all().last().id
        data = {
            'email': 'galan2@uc.cl',
        }

        response = self.client.put(f'/api/users/update/{id}', data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["email"], 'galan2@uc.cl')

    def test_update_unsuccesfull_does_not_exist(self):
        data = {
            'email': 'galan2@uc.cl',
        }
        CustomUser.objects.all().delete()

        response = self.client.put(f'/api/users/update/1', data, content_type='application/json')
        self.assertEqual(response.status_code, 404)
