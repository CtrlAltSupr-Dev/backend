from rest_framework import serializers
from .models import Teacher, Course


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
