from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from ..serializers import *


@api_view(['GET'])
def get_courses(request):
    try:
        data = Course.objects.all()
    except Course.DoesNotExist:
        return Response({"mensaje": "There are not courses yet"}, status=404)
    serializer = CourseSerializer(data, context={'request': request}, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_course(request, pk=None):
    try:
        data = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response({"mensaje": "Course does not exist"}, status=404)
    serializer = CourseSerializer(data, context={'request': request})
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_course(request, pk=None):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response({"mensaje": "Course does not exist"}, status=404)
    course.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
