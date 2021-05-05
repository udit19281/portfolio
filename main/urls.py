from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'main'

urlpatterns = [
    path('',views.index,name='home'),
    path('project/',views.project,name='project'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
]
