from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('add', views.add_recipe, name="add"),
    path('browse', views.browse_recipes, name="browse"),
    path('menu', views.menu_create, name="menu"),
    path('search', views.search_recipes, name="search"),
    path('favorite', views.favorite_recipe, name="favorite"),
    path('profile/<str:username>', views.profile, name="profile"),

    # API Routes
    path("delete", views.delete_recipe, name="delete")
]