from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..serializers import *


@api_view(['GET'])
def get_reviews(request):
    data = Review.objects.all()
    serializer = ReviewSerializer(data, context={'request': request}, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_review(request, pk=None):
    data = Review.objects.get(pk=pk)
    serializer = ReviewSerializer(data, context={'request': request})
    return Response(serializer.data)
