from rest_framework import serializers

class YoSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView""" 
    name = serializers.CharField(max_length=10)
      