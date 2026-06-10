from django.views.generic import RedirectView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('daftar/', views.daftar_mahasiswa, name='daftar_mahasiswa'),
    path('', RedirectView.as_view(url='daftar/')),
]