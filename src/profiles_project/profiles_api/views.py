from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """returns a list of APIView features."""

        an_apiview = [
            'uses HTTP methods as functions (get, post, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over you logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})