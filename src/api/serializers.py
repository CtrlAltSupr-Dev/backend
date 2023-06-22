from rest_framework import serializers
from .models import Teacher, Course, Review


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
    # user = serializers.PrimaryKeyRelatedField(read_only=True)
    # teacher = serializers.PrimaryKeyRelatedField(read_only=True)
    # course = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Review
        # fields = ('pk', 'user', 'teacher', 'course', 'ratingOrganization', 'ratingClass', 'ratingMaterial', 'comment', 'addedDate')
        fields = '__all__'