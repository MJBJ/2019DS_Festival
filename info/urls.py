from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('map', views.map),
    path('notice', views.notice),
    path('timetable', views.timetable),
    path('detail', views.detail),
    path('',views.dday, name='dday'),
]