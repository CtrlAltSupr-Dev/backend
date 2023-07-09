from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Avg

class Teacher(models.Model):
    name = models.CharField("Name", max_length=240)
    ratingOrganized = models.IntegerField()
    ratingCommunication = models.IntegerField()
    ratingMaterial = models.IntegerField()
    addedDate = models.DateField("Added Date", auto_now_add=True)
    courses = models.ManyToManyField('Course')

    def update_ratings(self):
        reviews = self.review_set.filter(approved=1)
        average_organization = reviews.aggregate(Avg('ratingOrganization'))['ratingOrganization__avg']
        average_class = reviews.aggregate(Avg('ratingClass'))['ratingClass__avg']
        average_material = reviews.aggregate(Avg('ratingMaterial'))['ratingMaterial__avg']

        self.ratingOrganized = round(average_organization) if average_organization else 0
        self.ratingCommunication = round(average_class) if average_class else 0
        self.ratingMaterial = round(average_material) if average_material else 0
        self.save()

    def __str__(self):
        return self.name


class Course(models.Model):
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
    
    ratingOrganization = models.IntegerField()
    ratingClass = models.IntegerField()
    ratingMaterial = models.IntegerField()
    comment = models.TextField("Comment")
    addedDate = models.DateField("Added Date", auto_now_add=True)
    
    APPROVAL_CHOICES = (
        (0, 'Pending'),
        (1, 'Approved'),
        (2, 'Rejected'),
    )
    approved = models.IntegerField(choices=APPROVAL_CHOICES, default=0)

    def __str__(self):
        return f"User:{self.user.id} | {self.course.name} | {self.teacher.name}"
