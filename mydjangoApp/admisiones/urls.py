from django.urls import path
from admisiones import views

urlpatterns = [
    path('', views.home , name='home'),
    path('admisiones', views.admision , name='admision'),
]