
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('cadastrar/', views.cadastrar_doacao, name='cadastrar'),
    path('entregas/', views.entregas, name='entregas'),
]
