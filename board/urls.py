
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('<int:board_id>',views.detail, name="detail"), # 글 하나 보여주기
    path('post/',views.boardpost, name='post'), # 글쓰기
    path('show/', views.show, name='show'), # 전체 게시글
    path('photo/', views.photo, name="photo"),
    path('delete/<int:board_id>', views.delete, name='delete'),
]