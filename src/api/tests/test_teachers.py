from django.test import TestCase, Client

from api.models import Teacher


class TeacherTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    # Get All
    def test_get_all_succesfull(self):
        Teacher.objects.create(name="Klapp", ratingOrganized=3, ratingCommunication=1, ratingMaterial=1).save()
        response = self.client.get('/api/teachers')

        self.assertNotEqual(len(response.data), 0)
        self.assertEqual(response.status_code, 200)

    def test_get_all_unsuccesfull_no_teachers(self):
        Teacher.objects.all().delete()
        response = self.client.get('/api/teachers')

        self.assertEqual(len(response.data), 0)

    # Get
    def test_get_succesfull(self):
        Teacher.objects.create(name="Klapp", ratingOrganized=3, ratingCommunication=1, ratingMaterial=1).save()
        id = Teacher.objects.all().last().id
        response = self.client.get(f'/api/teachers/details/{id}')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['ratingOrganized'], 3)
        self.assertEqual(response.data['ratingMaterial'], 1)

    def test_get_unsuccesfull_does_not_exist(self):
        Teacher.objects.all().delete()
        response = self.client.get(f'/api/teachers/details/{1}')

        self.assertEqual(response.status_code, 404)

    # Delete
    def test_delete_succesfull(self):
        id = Teacher.objects.all().last().id
        response = self.client.delete(f'/api/teachers/delete/{id}')

        self.assertEqual(response.status_code, 204)

    def test_delete_unsuccesfull_does_not_exist(self):
        Teacher.objects.all().delete()
        response = self.client.delete('/api/teachers/delete/1')

        self.assertEqual(response.status_code, 404)
