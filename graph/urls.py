from django.contrib import admin
from django.urls import path
from graph import views

urlpatterns = [
    path('line',views.line),
    path('bar',views.bar),
    path('hist',views.hist),
    path('pie',views.pie)
]