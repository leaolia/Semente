from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.pacientes, name='index'),  # Redireciona para a página de pacientes
    path('pacientes/', views.pacientes, name='pacientes'),  # Lista de pacientes
    path('adicionar/', views.adicionar_paciente, name='adicionar_paciente'),  # Adicionar Paciente
    path('atualizar/', views.att_paciente, name='att_paciente'),  # Atualizar Paciente
    path('relatorios/', views.relatorios, name='relatorios'),  # Relatórios
]
