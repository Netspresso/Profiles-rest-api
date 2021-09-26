from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    """Serlializers a name field for testing our APIView"""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ['id', 'email', 'name', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    # def update(self, instance, validated_data):
    #     """Handle updating user account"""
    #     if 'password' is validated_data:
    #         password = validated_data.pop('password')
    #         instance.set_password(password)

        # return instance

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes proflile feed items"""

    class Meta:
        model = models.ProflieFeedItem
        fields = [
            'id',
            'user_profile',
            'status_text',
            'created_on'
        ]
        extra_kwargs = {
            'user_profile': {'read_only': True}
        }
