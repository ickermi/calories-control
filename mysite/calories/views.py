from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("Hello world. You're at the calories control service")