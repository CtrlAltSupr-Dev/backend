from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from ..serializers import *


@api_view(['GET'])
def get_reviews(request):
    try:
        data = Review.objects.all()
    except Review.DoesNotExist:
        return Response({"mensaje": "There are no reviews yet"}, status=404)
    serializer = ReviewSerializer(data, context={'request': request}, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_review(request, pk=None):
    try:
        data = Review.objects.get(pk=pk)
    except Review.DoesNotExist:
        return Response({"mensaje": "Review does not exist"}, status=404)
    serializer = ReviewSerializer(data, context={'request': request})
    return Response(serializer.data)


@api_view(['POST'])
def create_review(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    

@api_view(['DELETE'])
def delete_review(request, pk=None):
    try:
        data = Review.objects.get(pk=pk)
    except Review.DoesNotExist:
        return Response({"mensaje": "Review does not exist"}, status=404)
    data.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def update_review(request, pk=None):
    try:
        data = Review.objects.get(pk=pk)
    except Review.DoesNotExist:
        return Response({"mensaje": "Review does not exist"}, status=404)
    
    serializer = ReviewSerializer(data, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)