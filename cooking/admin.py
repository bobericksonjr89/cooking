from django.contrib import admin
from .models import User, RecipeItem, Menu, UserProfile


# Register your models here.
admin.site.register(User)
admin.site.register(RecipeItem)
admin.site.register(Menu)
admin.site.register(UserProfile)