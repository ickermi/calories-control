from django.shortcuts import render, reverse, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import FoodCategory, Food
from .forms import UserRegistrationForm, EatenFoodForm


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
    food = Food.objects.all()
    return render(request, 'calculator.html', {'food': food})

@login_required
def add_eaten_food(request):
    if request.method == 'POST':
        form = EatenFoodForm(request.POST)
        if form.is_valid():
            eaten_food = form.save(commit=False)
            eaten_food.user_eaten = request.user
            eaten_food.save()
            request.session['calories'] = eaten_food.calculate_calories()
            return redirect(reverse('calc_result'))
    else:
        form = EatenFoodForm()

    return render(request, 'add_eaten_food.html', {'form': form})

def calc_result(request):
    return render(request, 'calc_result.html', {'calories': request.session['calories']})