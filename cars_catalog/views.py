from django.shortcuts import render, redirect, get_object_or_404
from .models import Car

# Create your views here.

def car_list(request):
    cars = Car.objects.all() 

    return render(request, 'cars_catalog/car_list.html', {'car_list' : cars})
    

def car_detail(request, pk):

    car= get_object_or_404(Car, pk=pk)

    return render(request, 'cars_catalog/car_detail.html', { 'car': car} )

