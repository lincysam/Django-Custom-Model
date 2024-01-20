from django.shortcuts import render
from account.models import User
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.exceptions import ValidationError
from account.serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.request import Request
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            #serialized_data = serializer.data
            status_code = status.HTTP_200_OK
            success = True
            message = "User created successfully"
        else:
            success = False
            status_code = status.HTTP_400_BAD_REQUEST
            message = serializer.errors
        
        response = {
            'success': success,
            'status_code': status_code,
            'message': message,
            'data': serializer.data
        }
        return Response({'response':response}, status = status_code)
    
     
    def list(self, request):
        user = request.user
        if user.is_authenticated:
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        
    
class LoginView(APIView):  
    permission_classes=[]

    def post(self,request:Request):
        email = request.data.get('email')
        password = request.data.get('password')     
        
        user =authenticate(email=email,password=password)

        if user is not None:
            response={
                "messege":"Login Successful",
                #"token":user.auth_token.key,
            }
            token,_ = Token.objects.get_or_create(user=user)
           # return Response(data=response,{'Token':str(token)},status=status.HTTP_200_OK)
            return Response({'status':True,'message':'User Login Successful','Token':str(token)}, status.HTTP_201_CREATED)
        else:
            return Response(data={'messege':"Invalid email or password" })

    def get(self,request:Request):
        content={
            "user":str(request.user),
            "auth":str(request.auth)
        }   
        return Response(data=content, status=status.HTTP_200_OK)