from django.urls import path
from . import views

urlpatterns = [
    path('', views.pacientes, name='pacientes'),  # Página inicial do app
]
