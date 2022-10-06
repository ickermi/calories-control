from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
    name = models.CharField(max_length=200)
    #measured in calories per 100 grams
    calories = models.FloatField()
    user_added = models.ForeignKey(User, on_delete=models.CASCADE)

class EatenFood(models.Model):
    name = models.ForeignKey(Food, on_delete=models.CASCADE)
    user_eaten = models.ForeignKey(User, on_delete=models.CASCADE)
    #measured in grams
    weight_eaten = models.FloatField()
    eating_time = models.DateTimeField()

