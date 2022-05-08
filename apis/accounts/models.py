import uuid
from django.db import models
from django.contrib.auth.models import User
from home.helpers import *

# Create your models here.

class UserProfile(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile          = models.CharField(max_length=100, blank=True, null=True)
    created_date 	= models.DateField(auto_now_add=True)
    updated_at 	    = models.DateField(auto_now=True)
    is_verified     = models.BooleanField(default=False)
    token           = models.CharField(max_length=255, blank=True, null=True)
    ip_address      = models.CharField(max_length=100, blank=True, null=True)
    user_agents     = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.user)

    # @property
    # def ip_address(self):
    #     return get_ip(request)

class PasswordRecovery(models.Model):
    class Meta:
        verbose_name_plural = 'Password Recovery'

    id                          = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    email                       = models.EmailField()
    reset_link                  = models.CharField(max_length=200)
    created_date                = models.DateTimeField(auto_now_add=True)
    ip_address                  = models.CharField(max_length=100, blank=True, null=True)
    user_agents                 = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.email)