from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('create/', views.TodolistCreate.as_view(), name='create')
]
