from django.urls import path
from . import views

urlpatterns = [   
    path('produdtos/', views.produtos, name ='index.html'),
]
