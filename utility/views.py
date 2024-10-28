from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def invoice(request):
    return HttpResponse("Invoice for utility") 

def backup(request):
    return HttpResponse("backup for utility")

def report(request):
    return HttpResponse("report for utility")

def restore(request):
    return HttpResponse("restore for utility")

