import threading
from async_timeout import timeout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache

from accounts.serializers import *
from accounts.models import *

CACHE_TTL = getattr(settings ,'CACHE_TTL' , DEFAULT_TIMEOUT)

# Create your views here.

class EmailThread(threading.Thread):
    def __init__(self, email, reset_link):
        self.email      = email
        self.reset_link = reset_link
        threading.Thread.__init__(self)

    def run(self):
        try:
            subject = 'Password Recovery'

            body    = "Hi " + str(self.email) +",<br><br>\
                We're sending you this email because you requested a password reset. Click on this link to create a new password:<br><br>\
                Password Reset Link: <br><br>" +"<a>"+ settings.SITE_URL+"/#/new-password/"+str(self.reset_link) +"</a>"+ "<br><br><br>\
                If you didn't request a password reset you can ignore this email. Your password will not be changed.<br><br>\
                Thanks & Regards,<br>\
                Team Demo"

            msg = EmailMessage(subject, body, settings.ADMIN_EMAIL, to=[self.email])
            msg.content_subtype = "html"
            msg.send()
        except Exception as e:
            print(e)

class RegisterAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data, context={'request': request})
            if serializer.is_valid():
                serializer.save()

                email = serializer.data['email']
                user_profile = UserProfile.objects.get(user__email = email)

                user_profile.ip_address  = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '')).split(',')[0].strip()
                user_profile.user_agents = request.META['HTTP_USER_AGENT']
                user_profile.save()

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
    # permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        try:
            data = request.data
            print(data)
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

class ForgetPasswordAPI(APIView):
    def get_object(self, reset_link):
        return PasswordRecovery.objects.get(reset_link=reset_link)

    def post(self, request):
        try:
            data = request.data
            data['reset_link']  = uuid.uuid4().hex
            data['ip_address']  = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '')).split(',')[0].strip()
            data['user_agents'] = request.META['HTTP_USER_AGENT']

            serializer = ForgetPasswordSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                email       = serializer.data['email']
                reset_link  = serializer.data['reset_link']
                cache.set('token', reset_link, timeout=CACHE_TTL)

                if not User.objects.filter(email = email).exists():
                    return Response({
                    'status':   400,
                    'message': 'Email Not Already!',
                    'data':     serializer.data
                })

                EmailThread(email, reset_link).start()
                
                return Response({
                    'status': 200,
                })

            return Response({
                'status':   400,
                'message': 'Something Went Wrong!',
                'data':     serializer.data
            })
            
        except Exception as e:
            print(e)

    def patch(self, request):
        try:
            data = request.data
            try:
                obj = self.get_object(data['reset_link'])
            except:
                return Response({
                'status':   400,
                'message': 'Invalid Token!',
            })

            if cache.get('token') is None:
                return Response({
                'status':   400,
                'message': 'Your password reset link has expired!'
                })
            else:
                User.objects.filter(email=obj.email).update(password=make_password(data['password']))
                obj.delete()
                
            return Response({
                'status': 200,
                'message': 'Password Reset Successfully. Login To Continue',
            })
        except Exception as e:
            print(e)

class RegisterAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data, context={'request': request})
            if serializer.is_valid():
                serializer.save()

                email = serializer.data['email']
                user_profile = UserProfile.objects.get(user__email = email)

                user_profile.ip_address  = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '')).split(',')[0].strip()
                user_profile.user_agents = request.META['HTTP_USER_AGENT']
                user_profile.save()

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

class UserAPI(APIView):    
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()

            return Response({
                'status':   400,
                'message': 'Something Went Wrong!',
                'data':     serializer.data
            })
            
        except Exception as e:
            print(e)

    def get(self, request):
        try:
            all_users = User.objects.all()
            serializer = UserSerializer(all_users,  many=True)
            
            return Response({
                    'status':   200,
                    'message': 'Registration Successfully!',
                    'data':     serializer.data
                })
            
        except Exception as e:
            print(e)