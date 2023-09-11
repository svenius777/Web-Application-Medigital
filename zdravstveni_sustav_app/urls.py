from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pocetna, name='pocetna'),
    path('notfound/', views.not_found),
    path('about/', views.about, name='about'),
    path('narudzba/', views.NarudzbaView.as_view(), name='narudzba'),
    path('termini/', views.termini, name='termini'),
    path('doktori/', views.doktori, name='doktori'),
    path('lokacije/', views.lokacije, name='lokacije'),
]