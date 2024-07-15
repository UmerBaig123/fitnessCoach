from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class user_foods(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    fat = models.IntegerField()
    protein = models.IntegerField()
    carbs = models.IntegerField()
    portion = models.IntegerField()
    portion_unit = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class log(models.Model):
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class log_foods(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    fat = models.IntegerField()
    protein = models.IntegerField()
    carbs = models.IntegerField()
    portion = models.IntegerField()
    portion_unit = models.CharField(max_length=100)
    time_added = models.TimeField(auto_now_add=True)
    log = models.ForeignKey(log, on_delete=models.CASCADE)
    def addFromObject(user_food,user):
        name = user_food.name
        calories = user_food.calories
        fat = user_food.fat
        protein = user_food.protein
        carbs = user_food.carbs
        portion = user_food.portion
        portion_unit = user_food.portion_unit
        log = log.objects.get(user=user,date=datetime.date.today())
        log_food = log_foods( name=name, calories=calories, fat=fat, protein=protein, carbs=carbs, portion=portion, portion_unit=portion_unit, log=log)
        log_food.save()
    