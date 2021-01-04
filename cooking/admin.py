from django.contrib import admin
from .models import User, RecipeItem, Complement, Menu

# Register your models here.
admin.site.register(User)
admin.site.register(RecipeItem)
admin.site.register(Complement)
admin.site.register(Menu)