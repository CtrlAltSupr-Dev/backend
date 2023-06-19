from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..serializers import *


@api_view(['GET'])
def get_teachers(request):
    data = Teacher.objects.all()
    serializer = TeacherSerializer(data, context={'request': request}, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_teacher(request, pk=None):
    data = Teacher.objects.get(pk=pk)
    serializer = TeacherSerializer(data, context={'request': request})
    return Response(serializer.data)
