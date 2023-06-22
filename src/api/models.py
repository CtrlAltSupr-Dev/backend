from django.db import models
from django.contrib.auth.models import AbstractUser

class Teacher(models.Model):
    # TODO: has_many courses
    name = models.CharField("Name", max_length=240)
    ratingOrganized = models.IntegerField()
    ratingCommunication = models.IntegerField()
    ratingMaterial = models.IntegerField()
    addedDate = models.DateField("Added Date", auto_now_add=True)
    courses = models.ManyToManyField('Course')

    def __str__(self):
        return self.name


class Course(models.Model):
    # TODO: has_many Teachers
    name = models.CharField("Name", max_length=240)
    description = models.TextField("Description")
    initials = models.CharField("Name", max_length=240)
    teachers = models.ManyToManyField('Teacher')

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

class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    ratingOrganization = models.FloatField()
    ratingClass = models.FloatField()
    ratingMaterial = models.FloatField()
    comment = models.TextField("Comment")
    addedDate = models.DateField("Added Date", auto_now_add=True)

    def __str__(self):
        return f"User:{self.user.id} | {self.course.name}"
