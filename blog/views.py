#from django.shortcuts import render

# Create your views here.
# import imp
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PostSerializer

from .models import Post


@api_view(['GET'])
# shows everything that is in the database

def posts_list(request): 
    querysest = Post.objects.all()
    serializer = PostSerializer(querysest, many=True)
    return Response(serializer.data)

