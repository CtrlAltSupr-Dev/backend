from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from ..serializers import *


@api_view(['GET'])
def get_reviews(request):
    try:
        data = Review.objects.all()
        user = request.user
        print(user)
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
    # user = request.user
    try:
        review = Review.objects.get(pk=pk)
        # if (review.user.id != user.id):
        #     return Response({"mensaje": "You are not the owner of this review"}, status=403)
    except Review.DoesNotExist:
        return Response({"mensaje": "Review does not exist"}, status=404)
    teacher = review.teacher
    approved = review.approved
    review.delete()
    if approved == 1:
        teacher.update_ratings()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def update_review(request, pk=None):
    # user = request.user
    try:
        review = Review.objects.get(pk=pk)
        # if (review.user.id != user.id):
        #     return Response({"mensaje": "You are not the owner of this review"}, status=403)
    except Review.DoesNotExist:
        return Response({"mensaje": "Review does not exist"}, status=404)
    
    serializer = ReviewSerializer(review, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        review.teacher.update_ratings()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
