from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='stamp'),
    path('quest1',views.quest1,name='quest1'),
    path('quest2',views.quest2,name='quest2'),
    path('quest3',views.quest3,name='quest3'),
    path('quest4',views.quest4,name='quest4'),
    path('quest5',views.quest5,name='quest5'),
    path('check',views.check,name='check'),
    path('clear',views.clear,name='clear'),    
    
]