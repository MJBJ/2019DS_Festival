from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('<int:quest_id>',views.quest,name='quest'),
    path('check',views.check,name='check'),
    path('clear',views.clear,name='clear'),    
    
]