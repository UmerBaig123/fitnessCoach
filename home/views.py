from django.shortcuts import render
from .models import food
from login.models import UserStats
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# Create your views here.

@login_required(login_url='/auth/login')
def HomeView(request):
    return render(request, 'home.html', {'foods':food.objects.all(),"user":request.user})
@login_required(login_url='/auth/login')
def LogView(request):
    return render(request, 'log.html', {"user":request.user})
@login_required(login_url='/auth/login')
def ProfileView(request):
    activityLevels = ["Very Low", "Low", "Moderate", "High", "Very High"]
    goalLevels = ["Lose Weight Fast","Lose Weight Slowly", "Maintain", "Gain Weight Slowly", "Gain Weight Fast"]        
    if UserStats.objects.filter(user=request.user).exists():
        data = UserStats.getUsersObject(request.user)
        return render(request, 'profile.html', {'foods':food.objects.all(),"user":request.user,"stats":data})
    else:
        return redirect('user_stats')