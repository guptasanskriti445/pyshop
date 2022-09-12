from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',{'products':products})

def new(request):
    return HttpResponse('New products')

def login(request):
    return render(request, 'login.html')

@login_required
def home(request):
    return render(request, 'home.html')