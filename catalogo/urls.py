from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='catalogo'),
    path('tipo/<str:tipo>/', views.lista_tipodeimovel_view, name='tipo-de-imovel'),
    path('imovel/<int:pk>/', views.info_imovel_view, name='info-imovel'),
    path('anunciar/', views.anunciar_imovel_view, name='anunciar'),
    path('meus-anuncios/', views.imoveis_usuario_view, name='meus-anuncios'),
]