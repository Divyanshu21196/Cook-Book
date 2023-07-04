from django.urls import path,include
from cook_bok_api import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('profile',views.UserProfileViewSet)
router.register('recipe',views.UserRecipeViewSet)

urlpatterns = [
    path('',include(router.urls)),
     path('login/',views.UserLoginToken.as_view()),
]