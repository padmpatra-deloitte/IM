from rest_framework import serializers
from .models import User
import re


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone_no', 'profile_picture']


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=50, required=True)
    password = serializers.CharField(max_length=50, required=True)

    class Meta:
        fields = ['email', 'password']


class RegisterSerializer(serializers.Serializer):
    # first_name = serializers.CharField(required=True, max_length=75)
    # last_name = serializers.CharField(required=True, max_length=75)
    name = serializers.CharField(required=True, max_length=75)
    email = serializers.CharField(required=True, max_length=75)
    password = serializers.CharField(required=True, max_length=75)

    class Meta:
        fields = [
            'name',
            'email',
            'password',
        ]

    @classmethod
    def validate_email(cls, value):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not (re.fullmatch(regex, value)):
            return False
        return True
