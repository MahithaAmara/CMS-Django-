from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return HttpResponse("Login for security") 

def logout(request):
    return HttpResponse("Logout for security")

def reset(request):
    return HttpResponse("reset for security")

