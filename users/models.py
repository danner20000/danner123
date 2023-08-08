from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(unique=True,null=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

# Create your models here.
