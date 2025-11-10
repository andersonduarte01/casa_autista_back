from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'administrador'

router = DefaultRouter()
router.register(r'', views.AdministradorViewSet, basename='administrador')

urlpatterns = [
    path('api/', include(router.urls)),
]