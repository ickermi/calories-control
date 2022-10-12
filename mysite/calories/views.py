from django.shortcuts import render
from .models import FoodCategory, Food

def home_page(request):
    category_food = {}
    for category in FoodCategory.objects.all():
        if food := Food.objects.filter(category=category).order_by('name'):
            category_food[category] = food
    return render(request, 'calories/home_page.html', {'category_food': category_food})