from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from . import models

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """returns a list of APIView features."""

        an_apiview = [
            'uses HTTP methods as functions (get, post, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over you logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with out name."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating and object."""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Patch request only updates field provided in the request."""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Deletes an object."""

        return Response({'method': 'delete'})


class HelloViewset(viewsets.ViewSet):
    """Test API ViewSet."""

    serialer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list,create,retrieve, update, partial update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'Message': 'Hello', 'A Viewset': a_viewset})

    def create(self, request):
        """Create a new hello message."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)

            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting an object by its id"""

        return Response({'http_method': 'get'})

    def update(self, request, pk=None):
        """Handles updating an object by its id"""

        return Response({'http_method': 'put'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object"""

        return Response({'http_method': 'patch'})

    def destroy(self, request, pk=None):
        """Handles deleting an object"""

        return Response({'http_method': 'delete'})

class UserProfileViewset(viewsets.ModelViewSet):
    """handles creating, reading and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

