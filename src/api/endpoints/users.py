from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

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

@api_view(['PUT'])
def update_user(request, pk=None):
    # user = request.user
    try:
        user = CustomUser.objects.get(pk=pk)
        # if (review.user.id != user.id):
        #     return Response({"mensaje": "You are not the owner of this review"}, status=403)
    except CustomUser.DoesNotExist:
        return Response({"mensaje": "User does not exist"}, status=404)
    
    serializer = CustomUserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
