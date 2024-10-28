from django.urls import path 
from . import views

urlpatterns =[ 
    path('invoice', views.invoice, name='invoice'),
    path('report', views.report, name = 'report'),
    path('backup', views.backup, name = 'backup'),
    path('restore', views.restore, name = 'restore'),
]