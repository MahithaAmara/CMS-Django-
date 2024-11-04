from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import *
# Create your views here.
def register(request):
    return HttpResponse("Registration for Accounts") 

def update(request):
    return HttpResponse("Update for Accounts") 

def delete(request):
    return HttpResponse("delete for Accounts") 

#ORM views
def register(request):
    if request.method == "POST":
        cname = request.POST.get('cname')
        date = request.POST.get('date')
        pno=request.POST.get('pno')
        accounts.objects.create(cname=cname,date=date,pno=pno)
        queryset = accounts.objects.all()

def update(request):
    if request.method == "POST":
        data=request.POST()
        cname = data.get('cname')
        date = data.get('date')
        pno = data.get('pno')

def delete(request,date):
    queryset = accounts.objects.get(date=date)
    queryset.delete()

