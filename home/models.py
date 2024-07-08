from django.db import models

# Create your models here.
class food(models.Model):
    food_name = models.CharField(max_length=100)
    food_description = models.TextField()
    food_calories = models.IntegerField()
    food_fat = models.IntegerField()
    food_protein = models.IntegerField()
    food_carbs = models.IntegerField()
    