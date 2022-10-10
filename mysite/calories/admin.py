from django.contrib import admin
from .models import Food, EatenFood, FoodCategory

admin.site.register(Food)
admin.site.register(EatenFood)
admin.site.register(FoodCategory)
