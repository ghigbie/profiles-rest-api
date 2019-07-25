from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers



class YoApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django Views',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]
        return Response(
            {
                'message': 'Yo!!!',
                'an_apiview': an_apiview
            }
        )
