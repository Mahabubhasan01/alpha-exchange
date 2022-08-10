from django.shortcuts import render
from django.contrib.auth.models import User
from api.serializers import UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

# Users all api here


@api_view(['GET', 'POST'])
def User_list(request):
    """
    List all code Users, or create a new User.
    """
    if request.method == 'GET':
        Users = User.objects.all()
        serializer = UserSerializer(Users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def users_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
