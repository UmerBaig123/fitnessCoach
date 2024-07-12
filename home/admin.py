from django.contrib import admin
from . import models
# Register your models here.
# class homeAdmin(admin.ModelAdmin):
#     list_display = ['food_name', 'food_description', 'food_calories', 'food_fat', 'food_protein', 'food_carbs']
admin.site.register(models.user_foods) 