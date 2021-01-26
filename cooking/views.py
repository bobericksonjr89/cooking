import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import markdown2

from .models import User, RecipeItem, UserProfile, Menu
from .forms import RecipeForm, MenuForm


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
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name'].capitalize()
            image = form.cleaned_data['image']
            prep_time = form.cleaned_data['prep_time']
            cook_time = form.cleaned_data['cook_time']
            servings = form.cleaned_data['servings']
            ingredients = form.cleaned_data['ingredients']
            directions = form.cleaned_data['directions']
            course = form.cleaned_data['course']
            cuisine = form.cleaned_data['cuisine'].capitalize()
            creator = request.user
            obj = RecipeItem(name=name, image=image, prep_time=prep_time, cook_time=cook_time,
                servings=servings, ingredients=ingredients, directions=directions, course=course,
                cuisine=cuisine, creator=creator)
            obj.save()
            return HttpResponseRedirect('/')

    else:
        form = RecipeForm(initial={
            'ingredients': '- 1 tbsp oil \n- Half of an onion',
            'directions': '1. Heat oil in a pan. \n2. Add onion to hot oil.'}
            )

    return render(request, 'cooking/add.html', {
        'form': form,
    })


def browse_recipes(request):

    menus = Menu.objects.all()

    # SETS are immutable, unordered ... should I order it alphabetically??
    cuisines = set(RecipeItem.objects.values_list('cuisine', flat=True))
    return render(request, 'cooking/browse.html', {
        "menus": menus,
        "cuisines": cuisines,
    })


def menu_create(request):
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['name']
            starter = form.cleaned_data['starter']
            first = form.cleaned_data['first']
            second = form.cleaned_data['second']
            side1 = form.cleaned_data['side1']
            side2 = form.cleaned_data['side2']
            side3 = form.cleaned_data['side3']
            dessert = form.cleaned_data['dessert']
            obj = Menu(creator=request.user, title=title, starter=starter, first=first, second=second, 
                side1=side1, side2=side2, side3=side3, dessert=dessert)
            obj.save()
            return HttpResponseRedirect('/')



    else: 
        form = MenuForm
    
    return render(request, 'cooking/menu.html', {
        'form': form
    })


def search_recipes(request):
    if request.method == "POST":
        search = request.POST["search-field"]
        if request.POST["search-radio"] == "recipe":
            results = RecipeItem.objects.filter(name__icontains=search)
            if not results:
                message = "Sorry, couldn't find any recipes matching that query."
                return render(request, 'cooking/search.html', {
                    "results": results,
                    "message": message
                })

        elif request.POST["search-radio"] == "ingredient":
            results = RecipeItem.objects.filter(ingredients__icontains=search)
            if not results:
                message = "Sorry, couldn't find any recipes with ingredients matching that query."
                return render(request, 'cooking/search.html', {
                    "results": results,
                    "message": message
                })

        elif request.POST["search-radio"] == "menu": 
            results = Menu.objects.filter(title__icontains=search)
            if not results:
                message = "Sorry, couldn't find any menus matching that query."
                return render(request, 'cooking/search.html', {
                    "results": results,
                    "message": message
                })

        return render(request, 'cooking/search.html', {
            "results": results,
        })

    else:
        return render(request, 'cooking/search.html')


def profile(request, username):
    user = User.objects.get(username=username)
    recipe_items = RecipeItem.objects.filter(creator=user)
    for recipe_item in recipe_items:
        recipe_item.ingredients = markdown2.markdown(recipe_item.ingredients)
        recipe_item.directions = markdown2.markdown(recipe_item.directions)

    return render(request, "cooking/profile.html", {
        'recipe_items': recipe_items
    })


def favorite_recipe(request):
    return

def delete_recipe(request):
    return

