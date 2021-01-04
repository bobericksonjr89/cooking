from django.contrib.auth.models import AbstractUser
from django.db import models
import djfractions


# Create your models here.
class User(AbstractUser):
    pass


class RecipeItems(models.Model):
    name = models.CharField(max_lenth=100)
    

class Compliments(models.Model):


class Menus(models.Model):