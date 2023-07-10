from django.test import TestCase, Client

from api.models import Course

class CourseTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    # Get All
    def test_get_all_succesfull(self):
        Course(name='Programación Avanzada', description='Curso de programación avanzada', initials='IIC2143').save()
        response = self.client.get('/api/courses')

        self.assertNotEqual(len(response.data), 0)
        self.assertEqual(response.status_code, 200)

    def test_get_all_unsuccesfull_no_courses(self):
        Course.objects.all().delete()
        response = self.client.get('/api/courses')

        self.assertEqual(len(response.data), 0)
    
    # Get
    def test_get_succesfull(self):
        Course(name='Programación Avanzada', description='Curso de programación avanzada', initials='IIC2143').save()
        id = Course.objects.all().last().id
        response = self.client.get(f'/api/courses/details/{id}')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['description'], 'Curso de programación avanzada')
        self.assertEqual(response.data['initials'], "IIC2143")

    def test_get_unsuccesfull_does_not_exist(self):
        Course.objects.all().delete()
        response = self.client.get(f'/api/courses/details/{1}')

        self.assertEqual(response.status_code, 404)

    # Delete
    def test_delete_succesfull(self):
        id = Course.objects.all().last().id
        response = self.client.delete(f'/api/courses/delete/{id}')

        self.assertEqual(response.status_code, 204)

    def test_delete_unsuccesfull_does_not_exist(self):
        Course.objects.all().delete()
        response = self.client.delete('/api/courses/delete/1')

        self.assertEqual(response.status_code, 404)