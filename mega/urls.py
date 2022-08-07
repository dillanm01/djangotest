from django.urls import path

from . import views

urlpatterns = [
    path('', views.megan, name='megan'),
    path('pretty/', views.prettymegan, name='megan'),
    path('g2048/', views.g2048, name='g2048'),
]