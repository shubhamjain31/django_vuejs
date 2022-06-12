from django.conf import settings
from django.contrib.sessions.middleware import SessionMiddleware
from django.http import QueryDict

import importlib, json
from urllib.parse import urlencode
from accounts.models import UserProfile

class CustomSessionMiddleware(SessionMiddleware):
    def process_request(self, request):
        # for mobile users or apis
        if 'HTTP_AUTHORIZATION' in request.META:
            # print('sjdk',request.META['HTTP_AUTHORIZATION'])
            authorization_key = request.META['HTTP_AUTHORIZATION'].split(' ')

            user = UserProfile.objects.get(token=authorization_key[1])
            # request.META['CSRF_COOKIE'] = request.META['HTTP_X_CSRFTOKEN']
            # request.META['HTTP_COOKIE'] = 'csrftoken='+request.META['HTTP_X_CSRFTOKEN'] + '; sessionid='+ request.META['HTTP_AUTHORIZATION']
            
            # engine = importlib.import_module(settings.SESSION_ENGINE)
            # session_key = authorization_key[0]
            # request.session = engine.SessionStore(session_key)
            request.session['user'] =  user.pk
        else:
            # for web users
            pass

class AppTypeMiddleware(SessionMiddleware):
    def process_request(self, request):
        # for mobile users
        if 'HTTP_AUTHORIZATION' in request.META:
            authorization_key = request.META['HTTP_AUTHORIZATION'].split('/')

            # when request coming from flutter
            if authorization_key[1] == 'POST':
                data            = urlencode(json.loads(request.body))
                request.POST    = QueryDict(data)
                request.POST = request.POST.copy()
                request.POST.update({'app_type': True})
            else:
                request.GET = request.GET.copy()
                request.GET.update({'app_type': True})
        else:
            # when request coming from django
            pass