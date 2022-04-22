from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile          = models.CharField(max_length=100, blank=True, null=True)
    created_date 	= models.DateField(auto_now_add=True)
    updated_at 	    = models.DateField(auto_now=True)
    is_verified     = models.BooleanField(default=False)
    token           = models.CharField(max_length=100, blank=True, null=True)
    ip_address      = models.CharField(max_length=100, blank=True, null=True)
    user_agents     = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.user)