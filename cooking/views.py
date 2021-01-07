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
    # get all recipes from db
    recipe_items = RecipeItem.objects.all()

    # loop to convert ingredients and directions from markdown into html
    for recipe_item in recipe_items:
        recipe_item.ingredients = markdown2.markdown(recipe_item.ingredients)
        recipe_item.directions = markdown2.markdown(recipe_item.directions)
        
    return render(request, "cooking/index.html", {
        "recipe_items": recipe_items
    })


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # password match check
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "cooking/register.html", {
                "message": "Passwords did not match."
            })

        # create user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "cooking/register.html", {
                "message": "Profile already exists with this username."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "cooking/register.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check authetication
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "cooking/login.html", {
                "message": "Could not validate username and/or password."
            })

    # render login page if request is not POST
    else:        
        return render(request, "cooking/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


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