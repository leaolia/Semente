from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pacientes/', include('pacientes.urls')),  # Para o app "pacientes"
    path('', include('pacientes.urls')),  # Redireciona '/' para o app "pacientes"
]
