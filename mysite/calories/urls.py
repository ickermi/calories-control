from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('profile/all_days/', views.all_days, name='all_days'),
    path('profile/date_detail/<str:date>/', views.date_detail, name='date_detail'),
    path('calculator/', views.calculator, name='calculator'),
    path('add_eaten_food/', views.add_eaten_food, name='add_eaten_food'),
]