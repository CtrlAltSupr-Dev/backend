from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..serializers import *


@api_view(['GET'])
def get_courses(request):
    data = Course.objects.all()
    serializer = CourseSerializer(data, context={'request': request}, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_course(request, pk=None):
    data = Course.objects.get(pk=pk)
    serializer = CourseSerializer(data, context={'request': request})
    return Response(serializer.data)