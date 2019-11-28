from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('login/', views.login,name='login'),
    path('', views.index,name='index'),
    path('contact/', views.contact,name='contact'),
    path('about/', views.about, name='about'),

    path('blog/', views.blog, name='blog'),
    path('doctor/', views.doctor, name='doctor'),
    path('elements/', views.elements, name='elements'),
    path('services/', views.services, name='services'),
    path('singleblog/', views.singleblog, name='singleblog'),
]

