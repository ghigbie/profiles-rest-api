from rest_framework import serializers
from profiles_api import models

class YoSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView""" 
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile"""
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }

        def create(self, validated_data):
            """Create and return a new user"""