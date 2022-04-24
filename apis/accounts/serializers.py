from rest_framework  import serializers
from django.contrib.auth.models import User
from accounts.models import *
import uuid

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            email    = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username    = serializers.CharField()
    password    = serializers.CharField()

class ForgetPasswordSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PasswordRecovery
        fields = ['email', 'reset_link', 'ip_address', 'user_agents']