from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def menu(request, name):
    dishes = {
        'pasta' : 'this is pasta',
        'cheeze' : 'this is cheeze'
    }
    return HttpResponse(f"Dish Name {name} Description: {dishes[name]}")
