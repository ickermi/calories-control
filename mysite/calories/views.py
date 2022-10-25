from django.shortcuts import render, redirect, HttpResponse
from .models import FoodCategory, Food
from django.contrib.auth import authenticate, login

def home_page(request):
    error = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            error = 'Неверное имя пользователя или пароль'
    category_food = {}
    for category in FoodCategory.objects.all():
        if food := Food.objects.filter(category=category).order_by('name'):
            category_food[category] = food
    data = {
        'category_food': category_food,
        'error': error,
    }
    return render(request, 'home_page.html', data)