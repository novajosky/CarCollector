from ast import Del
from dataclasses import fields
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car
from django.http import HttpResponse
# Create your views here.


# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cars_index(request):
  cars = Car.objects.all()
  return render(request, 'cars/index.html', { 'cars': cars })

def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  return render(request, 'cars/detail.html', { 'car': car })

#class-cased view (CBV)
class CarCreate(CreateView):
  model = Car
  fields = '__all__'

class CarUpdate(UpdateView):
  model = Car
  fields = '__all__'

class CarDelete(DeleteView):
  model = Car
  success_url = '/cars/'