from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    pass


class RecipeItem(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='images/')
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    servings = models.IntegerField()
    ingredients = models.TextField()
    directions = models.TextField()
    course = models.CharField(max_length=30)
    cuisine = models.CharField(max_length=30)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(RecipeItem, related_name='favorited')

    def __str__(self):
        return self.user


class Menu(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    starter = models.ForeignKey(RecipeItem, on_delete=models.SET_NULL, blank=True, null=True, related_name='starter_recipe')
    first = models.ForeignKey(RecipeItem, on_delete=models.SET_NULL, blank=True, null=True, related_name='first_recipe')
    second = models.ForeignKey(RecipeItem, on_delete=models.SET_NULL, blank=True, null=True, related_name='second_recipe')
    side1 = models.ForeignKey(RecipeItem, on_delete=models.SET_NULL, blank=True, null=True, related_name='side1_recipe')
    side2 = models.ForeignKey(RecipeItem, on_delete=models.SET_NULL, blank=True, null=True, related_name='side2_recipe')
    side3 = models.ForeignKey(RecipeItem, on_delete=models.SET_NULL, blank=True, null=True, related_name='side3_recipe')
    dessert = models.ForeignKey(RecipeItem, on_delete=models.SET_NULL, blank=True, null=True, related_name='dessert_recipe')

    def __str__(self):
        return self.title