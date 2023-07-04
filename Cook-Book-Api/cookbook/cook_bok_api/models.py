from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    ''''Manager for user profile'''

    def create_user(self,email,name,password=None):
        '''create a new user profile'''

        if not email:
            raise ValueError('User must have an email address')

        
        email = self.normalize_email(email)
        user = self.model(email = email,name = name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        '''create and save a super user'''
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser):

    USER_CHOICES = (
        ('AUTHOR','1'),
        ('ADMIN','2')
    )

    email = models.EmailField(max_length=250,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    user_role = models.CharField(
        max_length=20,
        choices=USER_CHOICES,
        default='1'
    )


    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        '''Retrieve full name of user'''
        return self.name

    def get_short_name(self):
        '''retrieve short name of user'''
        return self.name

    def __str__(self):
        '''represent string representation of the user'''
        return self.name


class RecipeMenu(models.Model):
    '''recipe create model'''

    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    user_role_profile = models.ForeignKey(                        
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE      
    )

    created_on = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        '''return the model as string'''
        return self.title


