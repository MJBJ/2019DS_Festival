from django.contrib import admin
from django.urls import path, include
from . import views
import board.views
import stamp.views 
urlpatterns = [
    # path('', views.main, name='main'),
    # path('map', views.map, name='map'),
    # path('notice', views.notice, name='notice'),
    # path('timetable', views.timetable, name='timetable'),
    # path('detail', views.detail, name='detail'),
    # path('dday',views.dday, name='dday'),
    # path('develop', views.develop, name='develop'),
    # path('board/', include('board.urls')),
    # path('stamp/', include('stamp.urls')),
    path('',views.dday, name='dday'),
]