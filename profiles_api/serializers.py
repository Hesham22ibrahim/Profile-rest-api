from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """serializes a user profile object"""
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email','name','password')
        extra_kwargs = {
        'password':{
            'write_only':True,
            'style':{'input_type':'password'}}}

    def create(self,vlidated_data):
        """ create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email = vlidated_data['email'],
            name = vlidated_data['name'],
            password = vlidated_data['password']
        )
        return user
