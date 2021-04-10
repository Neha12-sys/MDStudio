from django.contrib import admin
from django.urls import path
from Home import views 

urlpatterns = [
    path("", views.index, name='Home'),
    path("contact", views.contact, name='contact'),
    path("services", views.services, name='services'),
    path("designing", views.designing, name='designing'),
    path("resources", views.resources, name='resources'),
    path("MConnect", views.MConnect, name='MConnect'),
    path("chat",views.chat, name="chat"),
    path('chat1',views.chat1,name="chat1"),
]
