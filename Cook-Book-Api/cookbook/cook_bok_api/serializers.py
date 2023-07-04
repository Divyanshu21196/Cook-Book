from rest_framework import serializers
from cook_bok_api import models


class UserProfileSerializer(serializers.ModelSerializer):
    '''serializes a user object'''

    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password','user_role')
        extra_kwargs = {
            'password':{
                'write_only':True,
                 'style':{
                     'input_type':'password'
                 }
            }
        }

class UserRecipeSerializer(serializers.ModelSerializer):
    '''serializes the recipe object'''

    class Meta:
        model = models.RecipeMenu
        fields = ('id','user_role_profile','title','description','created_on')
        extra_kwargs = {
            'user_role_profile':{
                'read_only':True
            }
        }
