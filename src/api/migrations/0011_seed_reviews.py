# Generated by Django 4.2.2 on 2023-06-21 16:13

from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_custom_user(apps, schema_editor):
    
    User = apps.get_model('api', 'CustomUser')
    user = User(
        email_verified=True,
        username="ssoliva",
        password=make_password("Seba22##"),
        is_superuser=True,
        is_staff=True,
        email="sjolivare@uc.cl",
        is_active=True
    )
    user.save()

def create_test_reviews(apps, schema_editor):
    Review = apps.get_model('api', 'Review')
    Review(ratingOrganization=3, ratingClass=4, ratingMaterial=5, comment="Muy ordenado y cercano", course_id=1, teacher_id=1, user_id=1).save()
    Review(ratingOrganization=2, ratingClass=5, ratingMaterial=1, comment="Entusiasmado y dispuesto, pero muy desordenado", course_id=2, teacher_id=2, user_id=1).save()
    Review(ratingOrganization=1, ratingClass=2,ratingMaterial=5, comment="Lo unico bueno es su material", course_id=3, teacher_id=3, user_id=1).save()
    Review(ratingOrganization=5, ratingClass=5, ratingMaterial=5, comment="Increible este profesor", course_id=4, teacher_id=4, user_id=1).save()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_review'),
    ]

    operations = [
        migrations.RunPython(create_custom_user),
        migrations.RunPython(create_test_reviews)
    ]
