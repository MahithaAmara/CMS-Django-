from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add(request):
    return HttpResponse("add for Products") 

def modify(request):
    return HttpResponse("Modify for Products")

def delete(request):
    return HttpResponse("Delete for Products")

