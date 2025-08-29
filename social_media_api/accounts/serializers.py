from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    # followers = serializers.PrimaryKeyRelatedField(many)
    class Meta:
        model =  CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']