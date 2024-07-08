from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .utils import Conversions
from .models import UserStats
# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Check if the user exists in the database
        user = authenticate(request, username=username, password=password)
        # If the user exists
        if user is not None:
            login(request, user)
            if UserStats.objects.filter(user=user).exists():
                return redirect('profile')
            else:
                return redirect('user_stats')
        else:
            messages.error(request, 'Username or password is incorrect')
            return redirect('login_user')
    return render(request, 'login.html',{})   
def sign_up_user(request):
    if request.method == 'POST':
        form = request.POST
        username = form['username']
        password = form['password']
        password2 = form['passwordConf']
        email = form['email']
        if len(username) < 6:
            messages.error(request, 'Username must be at least 6 characters long')
            return redirect('sign_up_user')
        if len(password) < 6:
            messages.error(request, 'Password must be at least 6 characters long')
            return redirect('sign_up_user')
        if password != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('sign_up_user')
        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken')
            return redirect('sign_up_user')
        # Create the user
        user = User.objects.create_user(username=username,email=email, password=password)
        user.save()
        messages.success(request, 'Account created successfully')
        login(request, user)
        return redirect('user_stats')
    return render(request, 'signup.html',{})

@login_required(login_url='login_user')
def UserStatsView(request):
    activityLevels = ["Very Low", "Low", "Moderate", "High", "Very High"]
    goalLevels = ["Lose Weight Fast","Lose Weight Slowly", "Maintain", "Gain Weight Slowly", "Gain Weight Fast"]        
    context = {}
    if UserStats.objects.filter(user=request.user).exists():
        data = UserStats.getUsersObject(request.user)
        context = {"stats":data}
    if request.method == 'POST':
        form = request.POST
        weightUnit = form['weightUnit']
        age = form['age']
        weight = form['weight']
        height = form['height']
        gender = form['gender']
        if gender == "male":
            gender = 'M'
        else:
            gender = 'W'
        if not age or not weight or not height or not gender or not form['activity'] or not form['goal']:
            messages.error(request, 'Please fill in all fields')
            return redirect('user_stats')
        activity = activityLevels.index(form['activity'])
        goal = goalLevels.index(form['goal'])
        if weightUnit == 'LBs':
            weight = Conversions.lbs_to_kg(float(weight))
        else:
            try:
                age = int(age)
                weight = float(weight)
                height = float(height)
                activity = float(activity)
                goal = float(goal)
            except:
                messages.error(request, 'Please enter valid values')
                return redirect('user_stats')
        if age < 0 or weight < 0 or height < 0:
            messages.error(request, 'Please enter valid values')
            return redirect('user_stats')
        Ustats = UserStats.MakeObject(request.user,age,weight,height,gender,activity,goal)
        Ustats.save()
        return redirect('profile')
    return render(request, 'UserStats.html', context)