from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastrar_projeto, name='cadastrar_projeto'),
    path('lista/', views.lista_projetos, name='lista_projetos'),
]
