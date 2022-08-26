from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

class Dog: 
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age
    
dogs = [
    Dog('Winnie', 'Goldendoodle', 'cute', 1),
    Dog('Pudding', 'Mini Goldendoodle', 'small', 4),
    Dog('Gilbert', 'French Bulldog', 'thick', 3)
]

def home(request):
    return HttpResponse('hello')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', {'dogs': dogs})