from django.shortcuts import render
from django.views.generic import ListView
from .models import Dishes


# Create your views here.
class DishListView(ListView):
    model = Dishes
    template_name = 'Dish_list.html'
