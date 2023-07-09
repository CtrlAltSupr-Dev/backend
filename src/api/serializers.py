from rest_framework import serializers
from .models import CustomUser, Teacher, Course, Review

class CustomUserSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ('pk', 'username', 'email', 'password', 'groups', 'user_permissions', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined', 'users')

class TeacherSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = ('pk', 'name', 'ratingOrganized', 'ratingCommunication', 'ratingMaterial', 'addedDate', 'courses')


class CourseSerializer(serializers.ModelSerializer):
    teachers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('pk', 'name', 'description', 'initials', 'teachers')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'