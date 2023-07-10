from django.contrib import admin

from cook_bok_api import models
# Register your models here.

admin.site.register(models.UserProfile)
admin.site.register(models.RecipeMenu)

