from rest_framework  import serializers
from django.contrib.auth.models import User
from accounts.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'last_login', 'date_joined', 'id']
    
    def create(self, validated_data):
        user = User(
            username      = validated_data['username'],
            email         = validated_data['email'],
            first_name    = validated_data['first_name'],
            last_name     = validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def get_queryset(self):
        _id = self.kwargs['id']
        user = User.objects.get(id=_id)
        return user

class LoginSerializer(serializers.Serializer):
    username    = serializers.CharField()
    password    = serializers.CharField()

class ForgetPasswordSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PasswordRecovery
        fields = ['email', 'reset_link', 'ip_address', 'user_agents']