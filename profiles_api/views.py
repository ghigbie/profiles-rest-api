from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers



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