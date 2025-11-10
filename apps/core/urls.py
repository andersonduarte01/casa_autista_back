from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.Indice.as_view(), name='index'),
    path('autenticacao/api/login/', views.LoginView.as_view(), name='login'),
]