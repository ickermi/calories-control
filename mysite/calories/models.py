from django.db import models
from django.contrib.auth.models import User


class FoodCategory(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=200)
    #measured in calories per 100 grams
    calories = models.FloatField()
    user_added = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class EatenFood(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    user_eaten = models.ForeignKey(User, on_delete=models.CASCADE)
    #measured in grams
    weight_eaten = models.FloatField()
    eating_time = models.DateTimeField()

    def __str__(self):
        return str(self.food)

    def calculate_calories(self):
        return self.weight_eaten * self.food.calories / 100

