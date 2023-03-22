from django.contrib import admin
from django.urls import path

from accounts.views import signup

urlpatterns = [
    path('signup/', signup, name='signup')
]
