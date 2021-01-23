from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    return render(request, 'mywebsite/home.html', context)

def products(request):
    context = {}
    return render(request, 'mywebsite/products.html', context)

def people(request):
    context = {}
    return render(request, 'mywebsite/people.html', context) 

def contactus(request):
    context = {}
    return render(request, 'mywebsite/contactus.html', context) 
