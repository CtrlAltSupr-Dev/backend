from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from api.models import CustomUser, Review

class Command(BaseCommand):
    help = 'Create seeds for users and reviews'

    def handle(self, *args, **options):
        user = CustomUser(
            email_verified=True,
            username="fegalan",
            password=make_password("felipe_galan"),
            is_superuser=True,
            is_staff=True,
            email="galan@uc.cl",
            is_active=True
        )
        user.save()

        review = Review.objects.create(
            ratingOrganization=3.2,
            ratingClass=4,
            ratingMaterial=5,
            comment="Muy ordenado y cercano",
            course_id=1,
            teacher_id=1,
            user_id=1
        )
        review.save()