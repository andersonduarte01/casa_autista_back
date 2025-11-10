from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'funcionario'

router = DefaultRouter()
router.register(r'', views.FuncionarioViewSet, basename='funcionario')

urlpatterns = [
    path('api/', include(router.urls)),
]