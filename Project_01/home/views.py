from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login_page(request): 
    return HttpResponse("this is login page")

def home_page(request): 
    return HttpResponse("this is home page")

def logout_page(request , number): 
    return HttpResponse(f"this is dyanamic page {number}")