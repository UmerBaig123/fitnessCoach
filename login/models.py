from django.db import models
from django.contrib.auth.models import User
from .utils import BodyStats
import logging
logging.basicConfig(level=logging.DEBUG)
# Create your models here.
class UserStats(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    gender = models.CharField(max_length=1)
    activity = models.FloatField()
    goal = models.FloatField()
    BMI = models.FloatField()
    BMR = models.FloatField()
    CaloriesIntake = models.FloatField()
    ProteinIntake = models.FloatField()
    CarbsIntake = models.FloatField()
    FatIntake = models.FloatField()
    def MakeObject(user,age,weight,height,gender,activity,goal):
        caloricAddition = [-1000,-500,0,500,1000]
        thisBMR = BodyStats.BMR(weight,height,age,gender)
        calories = BodyStats.caloriesIntake(thisBMR,activity)+caloricAddition[int(goal)]
        if UserStats.objects.filter(user=user).exists():
            oldStats = UserStats.objects.get(user=user)
            oldStats.age = age
            oldStats.weight = weight
            oldStats.height = height
            oldStats.gender = gender
            oldStats.activity = activity
            oldStats.goal = goal
            oldStats.BMI = BodyStats.BMI(weight,height)
            oldStats.BMR = thisBMR
            oldStats.CaloriesIntake = calories
            oldStats.ProteinIntake = BodyStats.ProteinIntake(calories)
            oldStats.CarbsIntake = BodyStats.CarbsIntake(calories)
            oldStats.FatIntake = BodyStats.FatIntake(calories)
            return oldStats
        return UserStats(user=user,age=age,weight=weight,height=height,gender=gender,activity=activity,goal=goal,BMI=BodyStats.BMI(weight,height),BMR=thisBMR,CaloriesIntake = calories,ProteinIntake=BodyStats.ProteinIntake(calories),CarbsIntake=BodyStats.CarbsIntake(calories),FatIntake=BodyStats.FatIntake(calories))
    def getUsersObject(user):
        if UserStats.objects.filter(user=user).exists():
            activityLevels = ["Very Low", "Low", "Moderate", "High", "Very High"]
            goalLevels = ["Lose Weight Fast","Lose Weight Slowly", "Maintain", "Gain Weight Slowly", "Gain Weight Fast"]        
            data = UserStats.objects.get(user=user)
            if data.gender=='M':
                data.gender = 'male'
            else:
                data.gender = 'female'
            data.activity = activityLevels[int(data.activity)]
            data.goal = goalLevels[int(data.goal)]
            return data
        return False
    def __str__(self):
        return self.user.username