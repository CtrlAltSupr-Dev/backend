from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..serializers import *


@api_view(['GET'])
def get_users(request):
    print("get_users")
    data = CustomUser.objects.all()
    serializer = CustomUserSerializer(data, context={'request': request}, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_user(request, pk=None):
    data = CustomUser.objects.get(pk=pk)
    serializer = CustomUserSerializer(data, context={'request': request})
    return Response(serializer.data)