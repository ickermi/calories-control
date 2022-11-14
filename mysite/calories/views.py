from django.shortcuts import render, reverse, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import date
from .models import FoodCategory, Food, EatenFood
from .forms import UserRegistrationForm, EatenFoodForm, CalculatorForm


def home_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse('home_page'))
    else:
        form = AuthenticationForm()

    category_food = {}
    for category in FoodCategory.objects.all():
        if food := Food.objects.filter(category=category).order_by('name'):
            category_food[category] = food
    context = {
        'category_food': category_food,
        'form': form,
    }
    return render(request, 'home_page.html', context)

@login_required
def profile(request):
    target_time = timezone.now() - timezone.timedelta(days=7)
    food = EatenFood.objects.filter(eating_time__gte = target_time)
    date_calories = {}
    for f in food:
        date = f.eating_time.date()
        date_calories.setdefault(date)
        if date_calories[date]:
            date_calories[date] += f.calculate_calories()
        else:
            date_calories[date] = f.calculate_calories()

    context = {
        'date_calories': date_calories,
    }
    return render(request, 'profile.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect(reverse('home_page'))
    else:
        form = UserRegistrationForm()

    return render(request, 'registration.html', {'form': form})

def calculator(request):
    if request.GET.get('food') and request.GET.get('weight'):
        form = CalculatorForm(request.GET)
        if form.is_valid():
            calories = form.cleaned_data['weight'] * form.cleaned_data['food'].calories / 100
    else:
        form = CalculatorForm()
        calories = None
    return render(request, 'calculator.html', {'form': form, 'calories': calories})

@login_required
def add_eaten_food(request):
    if request.method == 'POST':
        form = EatenFoodForm(request.POST)
        if form.is_valid():
            eaten_food = form.save(commit=False)
            eaten_food.user = request.user
            eaten_food.save()
            return redirect(reverse('add_eaten_food'))
    else:
        form = EatenFoodForm()

    return render(request, 'add_eaten_food.html', {'form': form})