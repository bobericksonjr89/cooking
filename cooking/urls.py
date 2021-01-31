from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('add', views.add_recipe, name="add"),
    path('browse', views.browse_recipes, name="browse"),
    path('new_menu', views.menu_create, name="new_menu"),
    path('search', views.search_recipes, name="search"),
    path('favorite', views.favorite_recipe, name="favorite"),
    path('profile/<str:username>', views.profile, name="profile"),
    path('edit/<str:recipe_name>', views.edit_recipe, name="edit"),
    path('recipe/<str:recipe_name>', views.recipe_view, name="recipe"),
    path('menu/<str:menu_name>', views.menu_view, name="menu"),
    path('cuisine/<str:cuisine_name>', views.cuisine_view, name="cuisine"),
    path('course/<str:course_name>', views.course_view, name="course"),

    # API Routes
    path("delete", views.delete_recipe, name="delete")
]