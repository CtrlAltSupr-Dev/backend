from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Teacher
from .serializers import *


@api_view(['GET'])
def api_greet(request):
    data = Teacher.objects.all()
    serializer = TeacherSerializer(data, context={'request': request}, many=True)
    return Response(serializer.data)

