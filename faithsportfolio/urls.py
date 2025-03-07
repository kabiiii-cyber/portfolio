
from django.contrib import admin
from django.urls import path
from faithsportfolio import views

urlpatterns = [

path('home/', views.index,name='home'),
    path('service/', views.services,name='service'),
    path('starter/', views.starter,name='starter'),
    path('about/', views.about,name='about'),
    path('contact/', views.contacts,name='contacts'),
    path('gallery/', views.gallery,name='gallery'),
    path('gallary/', views.gallery_single,name='gallary'),
]
