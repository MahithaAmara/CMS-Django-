from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def register(request):
    return HttpResponse("Registration for Accounts") 

def update(request):
    return HttpResponse("Update for Accounts") 

def delete(request):
    return HttpResponse("delete for Accounts") 

