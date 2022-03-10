# posts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    path('group_list/', views.group_list),
    path('group/<slug:slug>/', views.group_posts),
]
