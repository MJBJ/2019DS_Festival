from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('map', views.map, name='map'),
    path('notice', views.notice, name='notice'),
    path('timetable', views.timetable, name='timetable'),
    path('detail', views.detail, name='detail'),
    #path('',views.dday, name='dday'),
    path('develop', views.develop, name='develop'),
]