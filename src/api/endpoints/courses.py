from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from ..serializers import *


@api_view(['GET'])
def get_courses(request):
    data = Course.objects.all()
    print("Data:", data)
    serializer = CourseSerializer(data, context={'request': request}, many=True)
    print("Serializado: ", serializer)
    return Response(serializer.data)


@api_view(['GET'])
def get_course(request, pk=None):
    data = Course.objects.get(pk=pk)
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
