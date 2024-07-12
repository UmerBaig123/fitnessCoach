from django.db import models
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
    date = models.DateField()
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
    def addFromObject(self, user_food):
        self.name = user_food.name
        self.calories = user_food.calories
        self.fat = user_food.fat
        self.protein = user_food.protein
        self.carbs = user_food.carbs
        self.portion = user_food.portion
        self.portion_unit = user_food.portion_unit