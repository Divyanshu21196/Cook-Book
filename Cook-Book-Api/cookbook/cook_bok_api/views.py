from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters 
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from cook_bok_api import serializers
from cook_bok_api import models
from cook_bok_api import permissions

# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)


class UserLoginToken(ObtainAuthToken):
    '''obtain token for the logged in user'''
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserRecipeViewSet(viewsets.ModelViewSet):
    '''viewset for reciept '''

    serializer_class = serializers.UserRecipeSerializer
    queryset = models.RecipeMenu.objects.all()
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (permissions.UpdateOwnRecipe,IsAuthenticated)


    def perform_create(self,serializer):
        '''set the user profile to logged in user'''
        serializer.save(user_role_profile = self.request.user)



