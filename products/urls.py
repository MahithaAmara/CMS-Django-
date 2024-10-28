from django.urls import path 
from . import views

urlpatterns =[ 
    path('add', views.add, name='add'),
    path('modify', views.modify, name = 'modify'),
    path('delete', views.delete, name = 'delete'),
]