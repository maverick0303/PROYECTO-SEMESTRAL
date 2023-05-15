from django.contrib import admin
from django.urls import path, include
from .views import tienda,bombo
urlpatterns = [
    path('',tienda,name="tienda"),
    path('bombo/',bombo,name="bombo"),
]