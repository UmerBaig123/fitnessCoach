"""
URL configuration for fitnesscoach project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from login.views import UserStatsView
from . import views
urlpatterns = [
    path('', views.ProfileView, name='home'),
    path('profile/', views.ProfileView, name='profile'),
    path('log/', views.LogView, name='log'),
    path('food/predefined/', views.FoodView, name='food'),
    path('food/add/', views.FoodAddView, name='add_food'),
    path('food/userdefined/', views.UserFoodView, name='user_food'),
    path('deletefood/', views.deleteUserFood.as_view()),
    path('UserStats/', UserStatsView, name='user_stats_home'),
]
