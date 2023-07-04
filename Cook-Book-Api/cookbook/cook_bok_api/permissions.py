from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    '''Allow user to edit their own profile'''

    def has_object_permission(self,request,view,obj):
        '''check whether the user is trying to udpate its own profile'''

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id



class UpdateOwnRecipe(permissions.BasePermission):
    '''allow user to edit there own added recipe'''

    def has_object_permission(self,request,view,obj):
        '''check if the user has the permission'''

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_role_profile.id == request.user.id