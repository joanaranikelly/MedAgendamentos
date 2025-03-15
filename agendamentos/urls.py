from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('clinicas/', views.lista_clinicas, name='lista_clinicas'),
]