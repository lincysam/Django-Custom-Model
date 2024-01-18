from rest_framework import serializers
from django.contrib.auth import password_validation
from django.conf import settings
from account.models import User

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