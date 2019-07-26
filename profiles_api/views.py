from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models

class YoApiView(APIView):
    """Test API View"""
    serializer_class = serializers.YoSerializer 

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

    def post(self, request):
        """Create a yo message with a name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Yo {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
    

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})


    def patch(self, request, pk=None):
        """Handle partial update of an object"""
        return Response({'method': 'PATCH'})


    def delete(self, request, pk=None):
        """Delete an object in a database"""
        return Response({'method': 'DELETE'})


class YoViewSets(viewsets.ViewSet):
    """Test API viewset"""
    serializer_class = serializers.YoSerializer

    def list(self, request):
        """Return a yo message"""

        a_viewset = [
            'Uses actions (list, create, retreive, update, partial_update, destry)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]
        return Response(
            {
                'message': 'Yo!!!!',
                'a_viewset' : a_viewset,
            }
        )

    def create(self, request):
        """Create a new yo message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Yo {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

