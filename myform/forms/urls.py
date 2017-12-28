from django.urls import path
from . import views

app_name='forms'
urlpatterns = [
    path('', views.entry, name='entry'),
    path('complete/', views.complete, name='complete'),
]