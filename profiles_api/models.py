from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.


class UserProfileManager(BaseUserManager):
    """docstring for UserProfileManager."""

    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email,name=name)
        user.setpassword(password)
        user.save(using=self._db)


 class UserProfile(AbstractBaseUser,PermissionsMixin):
     """docstring for UserProfile."""

     email = models.EmailField(max_lenth=255,unique=True)
     name - models.CharField(max_lenth=255)
     is_active = models.BoleanField(default=True)
     is_staff = models.BoleanField(default=True)

     objects = UserProfileManager()

     USERNAME_FIELD = 'email'
     REQUIRED_FIELD = ['name']


     def get_full_name(self):
     """retrive full name for users"""
        return self.name


     def get_short _name(self):
     """retrive short name for users"""
        return self.name

     def __str__(self):
         "return "

         return self.email
