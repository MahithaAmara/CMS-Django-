from django.urls import path 
from . import views

urlpatterns =[ 
    path('register', views.register, name='register'),
    path('update', views.update, name = 'update'),
    path('delete', views.delete, name = 'delete'),
]