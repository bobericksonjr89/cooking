from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    pass


class RecipeItem(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    servings = models.IntegerField()
    ingredients = models.TextField()
    directions = models.TextField()
    course = models.CharField(max_length=30)
    cuisine = models.CharField(max_length=30)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(RecipeItem, on_delete=models.CASCADE)
    

class Menu(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    starter = models.ForeignKey(RecipeItem, on_delete=models.SET_NULL, blank=True, null=True, related_name="starter_recipe")
    first = models.ForeignKey(RecipeItem, on_delete=models.SET_NULL, blank=True, null=True, related_name="first_recipe")
    second = models.ForeignKey(RecipeItem, on_delete=models.SET_NULL, blank=True, null=True, related_name="second_recipe")
    veg = models.ForeignKey(RecipeItem, on_delete=models.SET_NULL, blank=True, null=True, related_name="veg_recipe")
    dessert = models.ForeignKey(RecipeItem, on_delete=models.SET_NULL, blank=True, null=True, related_name="dessert_recipe")