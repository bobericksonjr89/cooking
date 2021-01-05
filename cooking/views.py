import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import markdown2

from .models import User, RecipeItem, Favorite, Menu


# Create your views here.
def index(request):
    return render(request, "cooking/index.html")


def register(request):
    return


def login_view(request):
    return


def logout_view(request):
    return


def add_recipe(request):
    return


def browse_recipes(request):
    return


def menu_create(request):
    return


def search_recipes(request):
    return


def favorite_recipe(request):
    return


def profile(request, username):
    return