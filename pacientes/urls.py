from django.urls import path
from . import views

urlpatterns = [
    path('', views.pacientes, name='pacientes'),  # Página inicial do app
    path('adicionar/', views.adicionar_paciente, name='adicionar_paciente'),
    path('atualizar/', views.att_paciente, name='att_paciente'),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('historico/', views.historico, name='historico'),
]
