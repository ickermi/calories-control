from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('registration/', views.registration, name='registration'),
    path('calculator/', views.calculator, name='calculator'),
    path('add_eaten_food/', views.add_eaten_food, name='add_eaten_food'),
    path('calculator_result/', views.calc_result, name='calc_result'),
]