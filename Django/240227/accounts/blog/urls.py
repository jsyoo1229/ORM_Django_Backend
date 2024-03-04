from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name= 'blog_list'),
    path('<int:pk>/', views.blog_detail, name= 'blog_detail'),
]

# 1.1 'blog/'                     : 블로그 글 목록
# 1.2 'blog/<int:pk>/'            : 블로그 상세 글 읽기