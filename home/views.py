from django.shortcuts import render
from .models import user_foods
from login.models import UserStats
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from dotenv import load_dotenv
from django.views.decorators.csrf import csrf_exempt
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
    if request.method == "POST":
        if not request.POST.get('name') or not request.POST.get('calories') or not request.POST.get('fat') or not request.POST.get('protein') or not request.POST.get('carbs') or not request.POST.get('portion') or not request.POST.get('portion_unit'):
            return redirect('user_food')
        user_food = user_foods()
        user_food.name = request.POST.get('name')
        user_food.calories = request.POST.get('calories')
        user_food.fat = request.POST.get('fat')
        user_food.protein = request.POST.get('protein')
        user_food.carbs = request.POST.get('carbs')
        user_food.portion = request.POST.get('portion')
        user_food.portion_unit = request.POST.get('portion_unit')
        user_food.user = request.user
        user_food.save()
        return redirect('user_food')
    foods = user_foods.objects.filter(user=request.user)
    page = request.GET.get('page', 1)
    query = request.GET.get('query', None)
    if int(page) < 1:
        page = 1
    if query is None or query == "":
        return render(request, 'user_food.html', {"user":request.user,"page":page,"search":False,"foods":foods})
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
class deleteUserFood(APIView):
    @csrf_exempt
    def get(self,request):
        # user_food = user_foods.objects.get(id=request.data.get('id'))
        # user_food.delete()
        return Response({"message":"hello man how are you"})
    @csrf_exempt    
    def post(self, request):
        user_food = user_foods.objects.get(id=request.data.get('id'))
        user_food.delete()
        return Response({"message":request.data.get('id')})