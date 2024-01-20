from rest_framework import serializers
from django.contrib.auth import password_validation
from django.conf import settings
from account.models import User
from rest_framework.authtoken.models import Token
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'email','password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self,validated_data):
        if User.objects.filter(username = validated_data['email']).exists():
            raise serializers.ValidationError("User with this email already exists")
        
        user = User.objects.create(
            
            username = validated_data['email'],
            email = validated_data['email'],
         
            )
        
        return user
    
    def create(self,validated_data):
        password = validated_data.pop('password')
        user=super().create(validated_data)
        user.set_password(password)
        user.save()

        Token.objects.create(user=user)
        return user