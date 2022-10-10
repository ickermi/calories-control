from django.shortcuts import render
from .models import Food

def home_page(request):
    food_list = Food.objects.order_by('name')
    return render(request, 'calories/home_page.html', {'food_list': food_list})