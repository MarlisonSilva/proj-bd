# app_django/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('atividade/adicionar/', views.adicionar_atividade, name='adicionar_atividade'),
    path('projeto/atualizar-lider/', views.atualizar_lider, name='atualizar_lider'),
    path('projetos/', views.listar_projetos, name='listar_projetos'),
    path('', views.home, name="home"),
]

