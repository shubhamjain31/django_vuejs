from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from .serializer import *

# Create your views here.

class RegisterAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()

                return Response({
                    'status':   200,
                    'message': 'Registration Successfully!',
                    'data':     serializer.data
                })
            
            return Response({
                    'status':   400,
                    'message': 'Something Went Wrong!',
                    'data':     serializer.errors
                })
        except Exception as e:
            print(e)

class LoginAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)
            if serializer.is_valid():
                username = serializer.data['username']
                password = serializer.data['password']

                user = authenticate(username=username, password=password)

                if user is None:
                    return Response({
                    'status':   400,
                    'message': 'Invalid Password!',
                    'data':     {}
                    })

                refresh = RefreshToken.for_user(user)
                print(refresh)
                return Response({
                    'status': 200,
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                })

            return Response({
                'status':   400,
                'message': 'Something Went Wrong!',
                'data':     serializer.data
            })
            
        except Exception as e:
            print(e)
