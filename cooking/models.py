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


class Complement(models.Model):
    recipe_a = models.ForeignKey(RecipeItem, on_delete=models.CASCADE, related_name="complemented")
    recipe_b = models.ForeignKey(RecipeItem, on_delete=models.CASCADE, related_name="complementee")


class Menu(models.Model):
    starter = models.ForeignKey(RecipeItem, on_delete=models.SET_NULL, blank=True, null=True, related_name="starter_recipe")
    first = models.ForeignKey(RecipeItem, on_delete=models.SET_NULL, blank=True, null=True, related_name="first_recipe")
    second = models.ForeignKey(RecipeItem, on_delete=models.SET_NULL, blank=True, null=True, related_name="second_recipe")
    veg = models.ForeignKey(RecipeItem, on_delete=models.SET_NULL, blank=True, null=True, related_name="veg_recipe")
    dessert = models.ForeignKey(RecipeItem, on_delete=models.SET_NULL, blank=True, null=True, related_name="dessert_recipe")