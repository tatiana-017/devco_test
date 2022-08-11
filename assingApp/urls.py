from django.urls import path
from assingApp import views

urlpatterns = [
    path('', views.assing, name="assing"),
]