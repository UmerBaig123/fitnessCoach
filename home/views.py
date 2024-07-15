from django.shortcuts import render
from .models import user_foods
from login.models import UserStats
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from dotenv import load_dotenv
import os
# Create your views here.

load_dotenv()
@login_required(login_url='/auth/login')
def HomeView(request):
    return render(request, 'home.html', {'foods':user_foods.objects.all(),"user":request.user})
@login_required(login_url='/auth/login')
def LogView(request):
    return render(request, 'log.html', {"user":request.user})
@login_required(login_url='/auth/login')
def FoodView(request):
    page = request.GET.get('page', 1)
    query = request.GET.get('query', None)
    usda_api_key = os.environ.get("API-KEY")
    if int(page) < 1:
        page = 1
    if query is None or query == "":
        return render(request, 'food.html', {"user":request.user,"page":page,"search":False,"usda_api_key":usda_api_key})
    else:
        return render(request, 'food.html', {"query":query,"page":page,"user":request.user,"search":True,"usda_api_key":usda_api_key})
@login_required(login_url='/auth/login')
def UserFoodView(request):
    page = request.GET.get('page', 1)
    query = request.GET.get('query', None)
    if int(page) < 1:
        page = 1
    if query is None or query == "":
        return render(request, 'user_food.html', {"user":request.user,"page":page,"search":False})
    else:
        return render(request, 'food.html', {"query":query,"page":page,"user":request.user,"search":True,"foods":foods})
@login_required(login_url='/auth/login')
def ProfileView(request):
    activityLevels = ["Very Low", "Low", "Moderate", "High", "Very High"]
    goalLevels = ["Lose Weight Fast","Lose Weight Slowly", "Maintain", "Gain Weight Slowly", "Gain Weight Fast"]        
    if UserStats.objects.filter(user=request.user).exists():
        data = UserStats.getUsersObject(request.user)
        return render(request, 'profile.html', {'foods':user_foods.objects.all(),"user":request.user,"stats":data})
    else:
        return redirect('user_stats')