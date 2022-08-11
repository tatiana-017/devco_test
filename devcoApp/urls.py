from django.urls import path
from devcoApp import views

urlpatterns = [
    path('', views.home, name="home"),
]
