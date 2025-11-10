from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls', namespace='core')),
    path('accounts/', include('apps.accounts.urls', namespace='accounts')),
    path('administrador/', include('apps.administrador.urls', namespace='administrador')),
    path('funcionario/', include('apps.funcionario.urls', namespace='funcionario')),
    path('paciente/', include('apps.paciente.urls', namespace='paciente')),
    path('responsavel/', include('apps.responsavel.urls', namespace='responsavel')),
    path('profissional/', include('apps.accounts.urls', namespace='profissional')),
]
