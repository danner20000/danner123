from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class UserManager(BaseUserManager):

        def create_user(self, username, email, password=None):

            user = self.model(
                username=username, 
                email=self.normalize_email(email)
                )
            user.set_password(password)
            user.save(using=self._db)

            return user

        def create_superuser(self, username, email, password):
            user = self.create_user(
                username=username,
                email=self.normalize_email(email),
                password=password
                )
            user.is_staff = True
            user.is_superuser = True
            user.save(using=self._db)
            return user

    objects = UserManager()

    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

# Create your models here.
