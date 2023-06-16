from django.db import models
from django.contrib.auth.models import AbstractUser

class Teacher(models.Model):
    name = models.CharField("Name", max_length=240)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    email_verified = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_users',  # Agrega un related_name personalizado
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_users',  # Agrega un related_name personalizado
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )