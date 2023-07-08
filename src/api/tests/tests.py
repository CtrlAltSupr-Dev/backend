from django.test import TestCase, Client
import unittest

from api.models import CustomUser, Teacher, Course, Review

class SimpleTest(unittest.TestCase):
    def test_register_fail_password2(self):
        client = Client()
        response = client.post("/register/", {
            "username": 'felipegalan',
            "email": "galan@uc.cl",
            "password1": "animated.13"})
        # print(response)
        self.assertEqual(response.status_code, 400)

    def test_register_fail_email(self):
        client = Client()
        response = client.post("/register/", {
            "username": 'felipegalan',
            "email": "galan@gmail.com",
            "password1": "animated.13",
            "password2": "animated.13"})
        # print(response)
        self.assertEqual(response.status_code, 400)
    
    def test_register_pass(self):
        client = Client()
        response = client.post("/register/", {
            'username': 'felipegalan',
            'email': 'galan@uc.cl',
            'password1': 'animated.13',
            'password2': 'animated.13'
        })
        # print(response)
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
        # print(response)
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
        # print(response)
        CustomUser.objects.filter(username="felipegalan").delete()
        self.assertEqual(response.status_code, 401)

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
        # print(response)
        CustomUser.objects.filter(username="felipegalan").delete()
        self.assertEqual(response.status_code, 200)



class ReviewTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username="felipegalan", email="galan@uc.cl", password="12345678", is_active=True, is_staff=False, is_superuser=False, email_verified=True)
        self.teacher = Teacher.objects.create(name="Klapp", ratingOrganized=3, ratingCommunication=1, ratingMaterial=1)
        self.course = Course.objects.create(name="Estructuras de Datos y Algoritmos", description="Curso de Algoritmos y Estructuras de Datos", initials="IIC2133")
        self.client = Client()

    # Create
    def test_create_succesfull(self):
        review = Review.objects.create(user=self.user, teacher=self.teacher, course=self.course, ratingOrganization=5, ratingClass=5, ratingMaterial=5, comment="Excelente curso y manejo del profesor")
        self.assertEqual(review.user, self.user)
        self.assertEqual(review.teacher, self.teacher)
        self.assertEqual(review.course, self.course)

    def test_create_unsuccesfull_missing_information(self):
        data = {
            'course': self.course.id,
            'teacher': self.teacher.id,
            'comment': 'Esta reseña no debería funcionar por falta de información'
        }

        response = self.client.post('/api/reviews/create', data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    # Get All
    def test_get_all_succesfull(self):
        Review(ratingOrganization=5, ratingClass=5, ratingMaterial=5, comment="Increible este profesor", course_id=4, teacher_id=4, user_id=1).save()
        response = self.client.get('/api/reviews')

        self.assertNotEqual(len(response.data), 0)
        self.assertEqual(response.status_code, 200)

    def test_get_all_unsuccesfull_no_reviews(self):
        Review.objects.all().delete()
        response = self.client.get('/api/reviews')

        self.assertEqual(len(response.data), 0)

    # Get
    def test_get_succesfull(self):
        Review(ratingOrganization=5, ratingClass=5, ratingMaterial=5, comment="Increible este profesor", course_id=4, teacher_id=4, user_id=1).save()
        id = Review.objects.all().last().id
        response = self.client.get(f'/api/reviews/details/{id}')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['ratingOrganization'], 5)
        self.assertEqual(response.data['comment'], "Increible este profesor")

    def test_get_unsuccesfull_does_not_exist(self):
        response = self.client.get(f'/api/reviews/details/{1000}')

        self.assertEqual(response.status_code, 404)

    # Update
    def test_update_succesfull(self):
        client = Client()
        user = client.login(username='ssoliva', password='Seba22##')
        Review(ratingOrganization=5, ratingClass=5, ratingMaterial=5, comment="Increible este profesor", course_id=4, teacher_id=4, user_id=1).save()
        id = Review.objects.all().last().id
        data = {
            'comment': 'Increible este profesor, pero ahora con una reseña actualizada',
            'user': user
        }

        response = self.client.patch(f'/api/reviews/update/{id}', data, content_type='application/json')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data["comment"], 'Increible este profesor, pero ahora con una reseña actualizada')

    def test_update_unsuccesfull_does_not_exist(self):
        data = {
            'comment': 'Increible este profesor, pero ahora con una reseña actualizada'
        }

        response = self.client.patch(f'/api/reviews/update/1000', data, content_type='application/json')
        self.assertEqual(response.status_code, 404)
    
    # Verificar que se calculan bien los ratings

    # Delete
    # def test_delete_succesfull(self):
        
    #     # Falta loggear acabo de cachar
    #     id = Review.objects.all().last().id
    #     print("ID:", id)
    #     response = self.client.delete(f'/api/reviews/delete/{id -1}')
    #     print("RESPONSE:", response)

    #     self.assertEqual(response.status_code, 204)

    def test_delete_unsuccesfull_does_not_exist(self):
        response = self.client.get('/api/reviews/delete/1000')

        self.assertEqual(response.status_code, 404)