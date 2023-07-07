from django.contrib import admin
from .models import CustomUser, Teacher, Course, Review 

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Review)
