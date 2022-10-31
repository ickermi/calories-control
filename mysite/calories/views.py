from django.shortcuts import render, reverse, redirect, HttpResponse
from .models import FoodCategory, Food
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm


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

    return render(request, 'registragion.html', {'form': form})